
from typing import Annotated
from fastapi import APIRouter, Depends
from app.domains.member.member_dependencies import get_follow_services
from app.domains.member.services import FollowServices

router = APIRouter(
   prefix="/users",
   tags=["Follow System"]
)



@router.get("/following")
async def get_following_list(follow_services: Annotated[FollowServices,Depends(get_follow_services)]):
   return await follow_services.get_following_list();

@router.get("/followers")
async def get_followers_list(follow_services: Annotated[FollowServices,Depends(get_follow_services)]):
   return await follow_services.get_follower_list();

@router.post("/{user_id}/follow")
async def user_follow(user_id:int,
                      follow_services: Annotated[FollowServices,Depends(get_follow_services)]):
   return await follow_services.user_follow(user_id)

@router.delete("/{user_id}/unfollow")
async def user_unfollow(user_id:int,
                      follow_services: Annotated[FollowServices,Depends(get_follow_services)]):
   return await follow_services.user_unfollow(user_id)


