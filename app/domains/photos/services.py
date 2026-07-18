


from app.domains.photos.repository import PhotoRepository


class PhotoServices:
   def __init__(self,photo_repository:PhotoRepository):
      self.photo_repository = photo_repository;
      pass
   async def upload_photo(self,photo):
      return await self.photo_repository.upload_photo(photo);
   async def delete_photo(self,photo_id):
      return await self.photo_repository.delete_photo(photo_id)
   async def get_all_photo(self):
      return await self.photo_repository.get_all_photo();
