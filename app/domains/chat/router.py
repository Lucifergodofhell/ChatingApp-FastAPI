import json
from typing import Annotated
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from app.domains.chat.chat_dependencies import get_chat_services
from app.domains.chat.services import ChatServices;


router = APIRouter(
   prefix="/chat",
   tags=["Chatting box"]
)


@router.websocket("/{user_id}")
async def start_chat(user_id:int,websocket:WebSocket,
                     chat_service:Annotated[ChatServices , Depends(get_chat_services)]):
   await chat_service.manager.connect(user_id,websocket);
   try:
      while True:
         data_str = await websocket.receive_text()
         data = json.loads(data_str);
         receiver_id = data.get("receiver_id")
         message = data.get("content")
         if receiver_id and message:
            await chat_service.process_new_message(
                                                sender_id=user_id,
                                                receiver_id=receiver_id,
                                                message=message)
   except WebSocketDisconnect:
      chat_service.manager.disconnect(user_id=user_id);