import cloudinary
from fastapi import HTTPException
from fastapi.concurrency import run_in_threadpool
from sqlalchemy import select
from app.core.config import get_settings
from app.core.database import Session
from app.domains.photos.photo_models import Photo
import cloudinary.uploader


setting = get_settings();

class PhotoRepository:
   def __init__(self,db:Session,user:dict):
      self.db=db;
      self.user = user;
   async def get_all_photo(self):
      if self.user is None:
         raise HTTPException(status_code=401,detail="Not able to get user");
      current_user_id = self.user.get('id');
      stmt = select(Photo).where(Photo.user_id == current_user_id)
      result = self.db.execute(stmt)
      photo_obj = result.scalars().all()
      return photo_obj

   
   async def upload_photo(self,photo):
      if not photo.content_type.startswith("image/"):
         raise HTTPException(status_code=400, detail="you can only upoload images")
      if self.user is None:
         raise HTTPException(status_code=401,detail="Not able to get user");
      current_user_id = self.user.get('id');
      folder_path=f"{setting.claudinary_folder_name}/users/user_{current_user_id}/photos"
      result = await run_in_threadpool(
         cloudinary.uploader.upload, 
         photo.file, 
         folder=folder_path
      )
      secure_url = result.get("secure_url")
      if not secure_url:
         raise HTTPException(status_code=500,detail="Your photo was not able to uploade");
      new_photo = Photo(image_url=secure_url, user_id=current_user_id,priority=0);
      self.db.add(new_photo)
      self.db.commit()
      return {"message":"Your photo has been Sucessfully uploaded"};

   async def delete_photo(self,photo_id):
      if self.user is None:
         raise HTTPException(status_code=401,detail="Not able to get user");
      current_user_id = self.user.get('id')
      stmt = select(Photo).where(Photo.id == photo_id, Photo.user_id == current_user_id)
      result = self.db.execute(stmt)
      photo_obj = result.scalars().first()
      if not photo_obj:
            raise HTTPException(status_code=404, detail="Photo not found or you don't have permission");
      try:
         url_parts = photo_obj.image_url.split('/upload/')
         if len(url_parts) == 2:
            path_without_version = url_parts[1].split('/', 1)[1]
            public_id = path_without_version.rsplit('.', 1)[0]
            await run_in_threadpool(cloudinary.uploader.destroy, public_id)
      except Exception as e:
         print(f"Cloudinary deletion issue: {e}")
      self.db.delete(photo_obj)
      self.db.commit()
      return {"message": "Your photo has been deleted Sucessfully"}

