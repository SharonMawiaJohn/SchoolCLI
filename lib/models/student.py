from sqlalchemy import Column, Integer, String
from lib.db import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    @classmethod
    def create(cls, db, name, email):
        student = cls(name=name, email=email)
        db.add(student)
        db.commit()
        db.refresh(student)
        return student
