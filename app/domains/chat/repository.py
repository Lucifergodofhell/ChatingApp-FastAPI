from app.core.database import Session
from app.domains.chat.chat_models import Chat


class ChatRepository:
   def __init__(self,db:Session):
      self.db=db
   
   async def save_messsage(self,sender_id,receiver_id,message):
      chat=Chat(
         sender_id = sender_id,
         receiver_id = receiver_id,
         message = message
      )
      self.db.add(chat);
      self.db.commit()
      self.db.refresh(chat)
      return chat;
      