from sqlalchemy import ForeignKey, Integer, String
from app.core.database import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship

class Photo(Base):
   __tablename__= 'photo'
   id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True);
   image_url:Mapped[str] = mapped_column(String(255),default=None);
   priority:Mapped[int] = mapped_column(Integer);
   user_id:Mapped[int] = mapped_column(Integer,ForeignKey("users.id"))
   user = relationship("User",back_populates="photos");




