from sqlalchemy import Column, Integer, String
from lib.db import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

    @classmethod
    def create(cls, db, title, description):
        course = cls(title=title, description=description)
        db.add(course)
        db.commit()
        db.refresh(course)
        return course
