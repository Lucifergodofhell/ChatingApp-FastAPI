from app.core.database import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Boolean, ForeignKey, Integer,String


class Friends(Base):
   __tablename__="friends"
   id:Mapped[int]= mapped_column(Integer,primary_key=True,index=True);
   follower_id:Mapped[int]=mapped_column(Integer,ForeignKey("users.id"))
   following_id:Mapped[int]=mapped_column(Integer,ForeignKey("users.id"))
   


