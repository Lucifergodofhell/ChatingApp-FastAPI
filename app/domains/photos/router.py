from typing import Annotated
from fastapi import APIRouter, Body, Depends, File, UploadFile

from app.domains.photos.photo_dependencies import get_photo_services
from app.domains.photos.services import PhotoServices;

router = APIRouter(
   prefix="/photo",
   tags=["Photo System"]
);

@router.get("/get-all-photo")
async def get_all_photo( photo_services:Annotated[PhotoServices,Depends(get_photo_services)],):
   return await photo_services.get_all_photo()


@router.post("/upload-photo")
async def upload_photo( photo_services:Annotated[PhotoServices,Depends(get_photo_services)],
                       photo:UploadFile = File(...),
                      ):
   return await photo_services.upload_photo(photo)


@router.delete("/delete-photo/{photo_id}")
async def delete_photo( photo_id:int,
                         photo_services:Annotated[PhotoServices,Depends(get_photo_services)],
                      ):
   return await photo_services.delete_photo(photo_id)


