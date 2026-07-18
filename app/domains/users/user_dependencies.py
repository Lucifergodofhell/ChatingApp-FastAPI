from typing import Annotated
from fastapi import Depends
from app.api.dependencies.dbdependency import get_db
from app.core.database import Session
from app.core.security import UserAuthentication, get_user_authentication
from app.domains.users.repository import UserRepository
from app.domains.users.services import UserServices


def ger_user_repository(db:Annotated[Session,Depends(get_db)],
                        security:Annotated[UserAuthentication,Depends(get_user_authentication)])->UserRepository:
   return UserRepository(db,security);

def get_user_services(repo:Annotated[UserRepository, Depends(ger_user_repository)])->UserServices:
   return UserServices(repo)