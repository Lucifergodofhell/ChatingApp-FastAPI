from sqlalchemy import create_engine
from app.core.config import get_settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


setting = get_settings()

engine = create_engine(setting.database_url);
Session = sessionmaker(autocommit=False,autoflush=False,bind=engine);
Base = declarative_base();

