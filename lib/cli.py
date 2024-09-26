from lib.db import get_db
from lib.helpers import create_course, list_courses, create_student, list_students, create_instructor, list_instructors

def main():
    while True:
        print("Please select an option:")
        print("0. Exit the program")
        print("1. Create a new course")
        print("2. List all courses")
        print("3. Create a new student")
        print("4. List all students")
        print("5. Create a new instructor")
        print("6. List all instructors")
        
        choice = input("> ")
        
        if choice == "0":
            break
        elif choice == "1":
            title = input("Enter course title: ")
            description = input("Enter course description: ")
            db = get_db()  # Get the DB session without using a context manager
            try:
                create_course(db, title, description)
            finally:
                db.close()  # Manually close the DB session
        elif choice == "2":
            db = get_db()  # Get the DB session
            try:
                courses = list_courses()
                for course in courses:
                    print(f"{course.id}: {course.title} - {course.description}")
            finally:
                db.close()
        elif choice == "3":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            db = get_db()
            try:
                create_student(db, name, email)
            finally:
                db.close()
        elif choice == "4":
            db = get_db()
            try:
                students = list_students(db)
                for student in students:
                    print(f"{student.id}: {student.name} - {student.email}")
            finally:
                db.close()
        elif choice == "5":
            name = input("Enter instructor name: ")
            email = input("Enter instructor email: ")
            db = get_db()
            try:
                create_instructor(db, name, email)
            finally:
                db.close()
        elif choice == "6":
            db = get_db()
            try:
                instructors = list_instructors(db)
                for instructor in instructors:
                    print(f"{instructor.id}: {instructor.name} - {instructor.email}")
            finally:
                db.close()
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

