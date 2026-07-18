from typing import Annotated
from fastapi import Depends
from app.core.security import UserAuthentication, get_user_authentication
from app.domains.auth.services import AuthServices
from app.domains.users.repository import UserRepository
from app.domains.users.user_dependencies import ger_user_repository


def get_auth_services(repo:Annotated[UserRepository, Depends(ger_user_repository)],
                      security:Annotated[UserAuthentication, Depends(get_user_authentication)]):
   return AuthServices(repo,security);