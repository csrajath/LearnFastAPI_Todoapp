from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# SQLALCHEMY_DATABASE_URL = "postgresql://task:task@localhost:5432/task"
SQLALCHEMY_DATABASE_URL = "postgresql://iwhsgausasqxtr:eb6535d17a9162b33a02628c3367962a2d58cb62fd0cb089ffc66d8b355269a7@ec2-3-225-213-67.compute-1.amazonaws.com:5432/dsfgi3s032864"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()