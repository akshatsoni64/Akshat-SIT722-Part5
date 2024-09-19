from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://admin:g9xYrNI3IoqBMwzZtck5BeV1JLk5ST5T@dpg-crlq9bjv2p9s73e2n3qg-a.singapore-postgres.render.com/task92d" # os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
