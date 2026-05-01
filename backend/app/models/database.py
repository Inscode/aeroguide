from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pgvector.sqlalchemy import Vector
from datetime import datetime
from dotenv import load_dotenv
import os




load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)
Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    document_type = Column(String(100), nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    
    chunks = relationship("DocumentChunk", back_populates="document", cascade="all, delete-orphan")

class DocumentChunk(Base):
    __tablename__ = "document_chunks"


    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    chunk_text = Column(Text, nullable=False)
    chunk_index = Column(Integer, nullable=False)
    page_number = Column(Integer, nullable=False)
    embedding = Column(Vector(384))

    document = relationship("Document", back_populates="chunks")

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)

    

