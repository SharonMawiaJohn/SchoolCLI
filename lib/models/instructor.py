from sqlalchemy import Column, Integer, String
from lib.db import Base

class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    @classmethod
    def create(cls, db, name, email):
        instructor = cls(name=name, email=email)
        db.add(instructor)
        db.commit()
        db.refresh(instructor)
        return instructor
