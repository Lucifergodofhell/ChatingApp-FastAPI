from typing import Annotated
from fastapi import Depends
from app.api.dependencies.auth_dependency import get_current_user
from app.api.dependencies.dbdependency import get_db
from app.core.database import Session
from app.domains.photos.repository import PhotoRepository
from app.domains.photos.services import PhotoServices

def get_photo_repository(db:Annotated[Session,Depends(get_db)],
                         user:Annotated[dict,Depends(get_current_user)]):
   return PhotoRepository(db,user)


def get_photo_services(repo:Annotated[PhotoRepository,Depends(get_photo_repository)]):
   return PhotoServices(repo);