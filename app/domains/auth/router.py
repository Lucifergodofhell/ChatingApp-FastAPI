from typing import Annotated
from fastapi import APIRouter, Body, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm;
from app.domains.auth.dependencies import get_auth_services
from app.domains.auth.services import AuthServices


router = APIRouter(
   prefix="/auth",
   tags=["auth"]
)

@router.post('/login')
async def user_login(auth_service: Annotated[AuthServices,Depends(get_auth_services)],
                     response:Response,
                     login_form:OAuth2PasswordRequestForm = Depends(),
                     ):
   return await auth_service.user_login(login_form,response);

@router.post('/logout')
async def user_logout(auth_service: Annotated[AuthServices,Depends(get_auth_services)],responcse:Response):
   return await auth_service.user_logout(responcse);