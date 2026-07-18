import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from app.core.database import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship

from app.domains.users.user_models import User

class Chat(Base):
   __tablename__="chat"
   id:Mapped[int] = mapped_column(Integer, primary_key=True,index=True);
   sender_id:Mapped[int] = mapped_column(ForeignKey("users.id"));
   receiver_id:Mapped[int] = mapped_column(ForeignKey("users.id"));
   message:Mapped[str] = mapped_column(String(300))
   created_at:Mapped[datetime.datetime] = mapped_column(DateTime,default=func.now());
   sender:Mapped["User"] = relationship("User",foreign_keys=[sender_id],
                                        backref="sent_messages")
   receiver:Mapped["User"] = relationship("User",foreign_keys=[receiver_id],
                                        backref="received_messages")