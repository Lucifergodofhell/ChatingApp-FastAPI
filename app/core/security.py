from datetime import timedelta, timezone
import datetime
import jwt
from app.core.config import get_settings
from passlib.context import CryptContext


setting = get_settings();
bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

class UserAuthentication:
   def __init__(self):
      pass

   def create_access_token(self,username:str,user_id:str,role:str,expire_delta:timedelta):
      encode = {'sub':username,'id':user_id,'role':role};
      expires =datetime.datetime.now(timezone.utc)+expire_delta;
      encode.update({'exp':expires});
      return jwt.encode(encode,setting.secret_key,algorithm=setting.jwt_algorithm);

   def create_refresh_token(self, username:str,user_id:int,expire_delta:timedelta):
      encode = {'sub':username,'id':user_id};
      expires = datetime.datetime.now(timezone.utc)+expire_delta
      encode.update({'exp':expires});
      return jwt.encode(encode,setting.secret_key,algorithm=setting.jwt_algorithm);

   def get_password_hash(self,password:str)->str:
      return bcrypt_context.hash(password);

   def verify_user_password(self,password:str,hashed_password)->bool:
      return bcrypt_context.verify(password,hashed_password);


def get_user_authentication():
   return UserAuthentication();