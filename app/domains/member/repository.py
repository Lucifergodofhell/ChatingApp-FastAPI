from fastapi import HTTPException
from sqlalchemy import delete, select
from app.core.database import Session
from app.domains.member.friends_model import Friends
from app.domains.users.user_models import User
from sqlalchemy.orm import selectinload


class FollowSystemRepository:
   def __init__(self,db:Session,user:dict):
      self.db =db;
      self.user=user;

   async def user_follow(self,user_id):
      if self.user is None:
         raise HTTPException(status_code=401,detail="Unauthorized request");
      if self.user.get('id') == user_id:
         raise HTTPException(status_code=400,detail="User can not follow himself");
      current_user_id = self.user.get('id')
      follow_check = select(Friends).where(Friends.follower_id == current_user_id , 
                                           Friends.following_id == user_id);
      result = self.db.execute(follow_check);
      user_obj = result.scalars().first();
      if user_obj is not None:
         raise HTTPException(status_code=400,detail="User already following");
      follow_request  = Friends(
         follower_id = self.user.get('id'),
         following_id = user_id
      )
      self.db.add(follow_request);
      self.db.commit();
      return {"message": f"Successfully followed user {user_id}"}
   
   
   async def user_unfollow(self,user_id):
      if self.user is None:
         raise HTTPException(status_code=401,detail="Unauthorized request");
      if self.user.get('id') == user_id:
         raise HTTPException(status_code=400,detail="User can not follow himself");
      current_user_id = self.user.get('id')
      stmt = delete(Friends).where(
          Friends.follower_id == current_user_id,
          Friends.following_id == user_id
      )
      result = self.db.execute(stmt)
      if result.rowcount == 0:
          raise HTTPException(status_code=400, detail="You are not following this user")
          
      self.db.commit()
      return {"message": f"Successfully removed user {user_id} from following list"}
   
   async def get_following_list(self):
      if self.user is None:
         raise HTTPException(status_code=401,detail="Unauthorized request");
      current_user_id = self.user.get('id')
      stmt = select(User).options(selectinload(User.following)).where(User.id == current_user_id)
      result =  self.db.execute(stmt)
      user_obj = result.scalars().first();
      return user_obj.following if user_obj else []
   
   async def get_follower_list(self):
      if self.user is None:
         raise HTTPException(status_code=401,detail="Unauthorized request");
      current_user_id = self.user.get('id')
      stmt = select(User).options(selectinload(User.followers)).where(User.id == current_user_id)
      result =  self.db.execute(stmt)
      user_obj = result.scalars().first();
      return user_obj.followers if user_obj else []







   