from app.domains.member.repository import FollowSystemRepository


class FollowServices:
   def __init__(self,follow_repository:FollowSystemRepository):
      self.follow_repository=follow_repository;

   async def user_follow(self,user_id):
      return await self.follow_repository.user_follow(user_id);
   async def user_unfollow(self,user_id):
      return await self.follow_repository.user_unfollow(user_id);
   async def get_following_list(self):
      return await self.follow_repository.get_following_list();
   async def get_follower_list(self):
      return await self.follow_repository.get_follower_list();







      