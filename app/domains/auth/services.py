from datetime import timedelta
from fastapi import HTTPException, Response
from app.core.security import UserAuthentication
from app.domains.users.repository import UserRepository


class AuthServices:
   def __init__(self,user_repository:UserRepository,security:UserAuthentication):
      self.user_repository = user_repository
      self.security = security

   async def user_login(self,loginForm,response:Response):
      user = await self.user_repository.get_userby_username(loginForm.username);
      if user is None:
         raise HTTPException(status_code=404,detail="No user was found with this username")
      is_pass_valid = self.security.verify_user_password(loginForm.password, user.hashed_password);
      if is_pass_valid is False:
         raise HTTPException(status_code=401,detail="Password is incorrect");
      else:
         refresh_token = self.security.create_refresh_token(user.username,user.id,timedelta(days=5));
         response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            samesite="lax",
            max_age=5*24*60*60,
            path="/"
         )
         access_token = self.security.create_access_token(
            username=user.username,
            user_id=user.id,
            role = user.role,
            expire_delta=timedelta(minutes=1)
         )
      return {
         'email':user.email,
         'username':user.username,
         'firstname':user.firstname,
         'lastname':user.lastname,
         'role':user.role,
         'is_active':user.is_active,
         'access_token':access_token,
         'token_type':'Bearer'
      }
   async def user_logout(self,response:Response):
      response.delete_cookie(
            key='refresh_token',
            httponly=True,
            samesite="lax",
            path="/"
      )
      return {"message": "Successfully logged out"}

      
