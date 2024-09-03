# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class NewsArticle(Base):
    __tablename__ = 'news_articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    image_link = Column(String)
    source_link = Column(String, unique=True, index=True)
    date_added = Column(DateTime, default=datetime.utcnow)


DATABASE_URL = "sqlite:///./news.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_database():
    Base.metadata.create_all(bind=engine)