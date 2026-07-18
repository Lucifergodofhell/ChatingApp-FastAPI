from app.api.dependencies import dbdependency
from app.domains.users.repository import UserRepository
from app.domains.users.schema import UserCreateRequest


class UserServices:
   def __init__(self,repository: UserRepository):
      self.repository = repository;
   
   async def create_user(self,user:UserCreateRequest):
      return await self.repository.create_user(user);
