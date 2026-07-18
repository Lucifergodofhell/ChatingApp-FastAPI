
from pydantic import AnyHttpUrl, BaseModel, EmailStr, Field

from app.domains.photos.photo_models import Photo


class UserCreateRequest(BaseModel):
   username:str = Field(min_length=3,max_length=30);
   email:EmailStr;
   first_name:str=Field(min_length=3,max_length=30);
   last_name:str=Field(min_length=3,max_length=30);
   image_url:AnyHttpUrl=Field(default=None);
   is_active:bool=Field(default=True);
   password:str =Field(min_length=5) ;
   role:str;
   model_config ={
      "json_schema_extra":{
         "example":{
            "username":"ravikumardhal",
            "email":"ravikumardhal@gmail.com",
            "first_name":"ravi",
            "last_name":"dhal",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/d/d8/Smiling_little_boy_of_Laos.jpg",
            "password":"Jaishrikrishna",
            "role":"user"
         }
      }
   }

