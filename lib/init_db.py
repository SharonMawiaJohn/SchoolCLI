from db import engine, Base
from models import course, student, instructor, enrollment  # Import all models

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized and tables created.")

if __name__ == "__main__":
    init_db()
