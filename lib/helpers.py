from lib.models.course import Course
from lib.models.student import Student
from lib.models.instructor import Instructor
from lib.models.enrollment import Enrollment
from lib.db import SessionLocal

def create_course():
    title = input("Enter course title: ")
    description = input("Enter course description: ")
    db = SessionLocal()
    Course.create(db, title, description)
    print("Course created.")

def list_courses():
    db = SessionLocal()
    courses = Course.get_all(db)
    for course in courses:
        print(f"{course.id}: {course.title} - {course.description}")

def create_student():
    name = input("Enter student name: ")
    db = SessionLocal()
    Student.create(db, name)
    print("Student created.")

def list_students():
    db = SessionLocal()
    students = Student.get_all(db)
    for student in students:
        print(f"{student.id}: {student.name}")

def create_instructor():
    name = input("Enter instructor name: ")
    db = SessionLocal()
    Instructor.create(db, name)
    print("Instructor created.")

def list_instructors():
    db = SessionLocal()
    instructors = Instructor.get_all(db)
    for instructor in instructors:
        print(f"{instructor.id}: {instructor.name}")

def enroll_student():
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    db = SessionLocal()
    Enrollment.create(db, student_id, course_id)
    print("Student enrolled.")

def exit_program():
    print("Goodbye!")
    exit()
