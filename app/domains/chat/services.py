from app.domains.chat.connection import ConnectionManager
from app.domains.chat.repository import ChatRepository


class ChatServices:
   def __init__(self,manager:ConnectionManager,chatrepository:ChatRepository):
      self.manager =manager;
      self.chatrepository = chatrepository

   async def process_new_message(self,sender_id:int,receiver_id :int,message:str):
      saved_message = await self.chatrepository.save_messsage(sender_id,receiver_id,message);
      message_data = {
            "id": saved_message.id,
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "message": saved_message.message,
            "created_at": str(saved_message.created_at)
        }
      await self.manager.send_personal_message(message_data,receiver_id);
      return message_data

      
      