

from fastapi import HTTPException, WebSocket


class ConnectionManager:
   def __init__(self):
      self.active_connections:dict[str,WebSocket]={}
   
   async def connect(self,user_id:int,websocket:WebSocket):
      await websocket.accept();
      self.active_connections[str(user_id)]=websocket;
   
   def disconnect(self,user_id:int):
      self.active_connections.pop(str(user_id),None);

   async def send_personal_message(self,message,receiver_id:int):
      receiver_websocket = self.active_connections.get(str(receiver_id));
      ## If user is offlien than we have to store this in database 
      if receiver_websocket:
         await receiver_websocket.send_json(message);

chat_manager = ConnectionManager()