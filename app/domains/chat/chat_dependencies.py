from typing import Annotated

from fastapi import Depends
from app.api.dependencies.dbdependency import get_db
from app.core.database import Session
from app.domains.chat.repository import ChatRepository
from app.domains.chat.services import ChatServices
from app.domains.chat.connection import chat_manager


def get_chat_repository(db:Annotated[Session,Depends(get_db)]):
   return ChatRepository(db);

def get_chat_services(chatrepository:Annotated[ChatRepository,Depends(get_chat_repository)]):
   return ChatServices(chat_manager,chatrepository)