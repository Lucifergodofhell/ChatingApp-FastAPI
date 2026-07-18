import cloudinary
from django.conf import Settings
from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache


class Setting(BaseSettings):
   app_name:str = "Tinder App";
   database_url:str;
   secret_key:str;
   jwt_algorithm:str;
   claudinary_api_secret:str;
   claudinary_api_key:str;
   claudinary_key_name:str;
   claudinary_folder_name:str;
   claudinary_cloud_name:str;
   model_config = SettingsConfigDict(env_file=".env",env_file_encoding="utf-8")

@lru_cache
def get_settings():
   return Setting();

settings = get_settings()
cloudinary.config(
    cloud_name=settings.claudinary_cloud_name,
    api_key=settings.claudinary_api_key,
    api_secret=settings.claudinary_api_secret
)
