from typing import Annotated

from fastapi import Depends
from app.api.dependencies.dbdependency import get_db
from app.core.database import Session
from app.core.security import UserAuthentication
from app.domains.users.schema import UserCreateRequest
from app.domains.users.user_models import User


class UserRepository:
   def __init__(self,db:Session,security:UserAuthentication):
      self.db = db;
      self.security = security
   
   async def create_user(self,createUserRequest:UserCreateRequest):
      user = User(
         email = createUserRequest.email,
         username=createUserRequest.username,
         firstname=createUserRequest.first_name,
         lastname = createUserRequest.last_name,
         hashed_password= self.security.get_password_hash(createUserRequest.password),
         role = createUserRequest.role.lower(),
         image_url=createUserRequest.image_url,
         is_active=True,
         photos=[]
      ); 
      self.db.add(user);
      self.db.commit()
      self.db.refresh(user)
      return user;
   async def get_userby_username(self,username:str):
      user = self.db.query(User).filter(User.username == username).first();
      return user;
   async def get_userby_id(self,id):
      user = self.db.query(User).filter(User.id == id).first();
      return user;


