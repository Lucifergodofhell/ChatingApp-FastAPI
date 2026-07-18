from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from fastapi import HTTPException

from app.core.config import get_settings


oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/login');
setting = get_settings();



def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
   try:
      payload = jwt.decode(token,setting.secret_key,setting.jwt_algorithm);
      username:str = payload.get('sub')
      userid:str = payload.get('id')
      if username is None or userid is None:
         raise HTTPException(status_code=401,detail="can not get user from token");
      return {
         'username':username,
         'id':userid,
         'role':payload.get('role')
      }
   except jwt.ExpiredSignatureError:
      raise HTTPException(
            status_code=401, 
            detail="Token has expired" 
        )
   except jwt.DecodeError:
      raise HTTPException(status_code=401,detail="can not get the user");
   except:
      raise HTTPException(status_code=401,detail="User not valid");


