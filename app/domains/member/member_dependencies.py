from typing import Annotated
from fastapi import Depends
from app.api.dependencies.auth_dependency import get_current_user
from app.api.dependencies.dbdependency import get_db
from app.core.database import Session
from app.domains.member.repository import FollowSystemRepository
from app.domains.member.services import FollowServices


def get_follow_repository(db:Annotated[Session,Depends(get_db)],user:Annotated[dict,Depends(get_current_user)]):
   return FollowSystemRepository(db,user);

def get_follow_services(repo:Annotated[FollowSystemRepository,Depends(get_follow_repository)]):
   return FollowServices(repo)

