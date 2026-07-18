from fastapi import APIRouter, Body, Depends
from app.api.dependencies import dbdependency
from app.domains.users.services import UserServices
from app.domains.users.schema import UserCreateRequest
from app.domains.users.user_dependencies import get_user_services;


router = APIRouter(
   prefix="/user",
   tags=["user"]
);

@router.post("/create_user")
async def create_user(user:UserCreateRequest=Body(),
                      user_services:UserServices=Depends(get_user_services)):
   return await user_services.create_user(user=user);
