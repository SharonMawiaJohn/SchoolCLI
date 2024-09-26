from models.course import Course
from models.student import Student
from models.instructor import Instructor
from models.enrollment import Enrollment
from lib.db import Base, engine

# Create the database tables
def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created.")

# Add some test data
def add_test_data():
    # Create instructors
    Instructor.create("John Doe")
    Instructor.create("Jane Smith")

    # Create courses
    Course.create("Python 101", "An introduction to Python programming.")
    Course.create("Data Science", "Learn the basics of data science.")

    # Create students
    Student.create("Alice Johnson")
    Student.create("Bob Brown")

    # Enroll students in courses
    Enrollment.create(1, 1)  # Enroll Alice in Python 101
    Enrollment.create(2, 2)  # Enroll Bob in Data Science

    print("Test data added.")

if __name__ == "__main__":
    create_tables()
    add_test_data()
