from typing import List
from sqlalchemy import Boolean, DateTime, Integer, String, func
from app.core.database import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
import datetime
from app.domains.photos.photo_models import Photo

class User(Base):
   __tablename__= 'users'
   id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True);
   username:Mapped[str] = mapped_column(String(50),unique=True);
   email:Mapped[str] = mapped_column(String(200),unique=True);
   firstname:Mapped[str]= mapped_column(String(50));
   lastname:Mapped[str]= mapped_column(String(50));
   image_url:Mapped[str] = mapped_column(String(255),nullable=True,default=None);
   is_active:Mapped[bool] = mapped_column(Boolean,default=True);
   created_at:Mapped[datetime.datetime] = mapped_column(DateTime,default=func.now());
   hashed_password:Mapped[str] = mapped_column(String(200));
   role:Mapped[str] = mapped_column(String(50));
   photos:Mapped[List["Photo"]] =relationship("Photo", back_populates="user",cascade="all,delete-orphan");
   following = relationship("User",
                            secondary="friends",
                            primaryjoin="Friends.follower_id == User.id",
                            secondaryjoin="Friends.following_id == User.id",
                            backref="followers"
                            )


