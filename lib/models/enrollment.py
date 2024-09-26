from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from lib.db import Base
from lib.models.course import Course
from lib.models.student import Student

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

# Adding back references
Student.enrollments = relationship("Enrollment", back_populates="student")
Course.enrollments = relationship("Enrollment", back_populates="course")
