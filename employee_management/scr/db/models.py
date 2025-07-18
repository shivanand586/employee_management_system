from sqlalchemy import create_engine, Column, Integer, String, Float
from os import getcwd
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger

engine = None 
Base = declarative_base()
DBsession = None

class EmployeeInfo(Base):
    __tablename__ = 'employee_info'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    department = Column(String, nullable=True)
    position = Column(String, nullable=True)
    salary = Column(Float, nullable=True)

def init_db():
    try: 
        global DBsession

        engine = create_engine(f"sqlite:///{getcwd()}/config/employee.db")
        conn = engine.connect()
        conn.close()
        Base.metadata.create_all(bind=engine)
        DBsession = sessionmaker(bind=engine)
        return DBsession
    except Exception as e:
        logger.error(f"Error occurred in init_db - {e}")
        return False

def get_session():
    if DBsession != None:
        session = DBsession()
        return session
    else:
        return None
    