from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

DATABASE_URL = "mysql+pymysql://root:Manish%40123@127.0.0.1:3306/university"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# ---------- Courses Table ----------
class Courses(Base):
    __tablename__ = "courses"

    cur_id = Column(Integer, primary_key=True, autoincrement=True)
    cur_name = Column(String(100), nullable=False)
    credits = Column(Integer, nullable=False)
    dep_id = Column(Integer)  # Can be null (no foreign key enforced)

Base.metadata.create_all(bind=engine)

# ---------- Pydantic Model ----------
class CourseCreate(BaseModel):
    cur_id: int 
    cur_name: str
    credits: int
    dep_id: int | None = None

# ---------- FastAPI App ----------
app = FastAPI()

# Create a new course
@app.post("/courses/")
def create_course(course: CourseCreate):
    db = SessionLocal()
    new_course = Courses(
        cur_id=course.cur_id,
        cur_name=course.cur_name,
        credits=course.credits,
        dep_id=course.dep_id
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    db.close()
    return {"message": "Course added successfully", "id": new_course.cur_id}

# Get all courses
@app.get("/courses/")
def get_courses():
    db = SessionLocal()
    courses = db.query(Courses).all()
    db.close()
    return courses
