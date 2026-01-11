from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, Date, Enum, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import date
import enum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"] if using VSCode Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ MySQL Connection
DATABASE_URL = "mysql+pymysql://root:Manish%40123@127.0.0.1:3306/university"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# ✅ Enum class for status
class StatusEnum(str, enum.Enum):
    active = "active"
    inactive = "inactive"
    alumni = "alumni"

# ✅ SQLAlchemy model — matches EXACT MySQL columns
class Student(Base):
    __tablename__ = "student"
    stu_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    First_name = Column(String(100), nullable=False)
    Last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    Phone = Column(String(10))
    dob = Column(Date)
    enrolment_date = Column(Date)  
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.active)


# ✅ Pydantic schema for requests
class StudentCreate(BaseModel):
    First_name: str
    Last_name: str
    email: str
    Phone: str
    dob: date
    enrolment_date: date
    status: StatusEnum

    class Config:
        orm_mode = True

# ✅ FastAPI app

# ✅ POST - Add student
@app.post("/students/", response_model=StudentCreate)
def create_student(student: StudentCreate):
    db = SessionLocal()
    db_student = Student(
        First_name=student.First_name,
        Last_name=student.Last_name,
        email=student.email,
        Phone=student.Phone,
        dob=student.dob,
        enrolment_date=student.enrolment_date,
        status=student.status
    )
    try:
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        print(f"✅ Added student ID: {db_student.stu_id}")
    except Exception as e:
        db.rollback()
        print("❌ Database Error:", e)
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
    return student

# ✅ GET - View all students
@app.get("/students/")
def read_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return [
        {
            "stu_id": s.stu_id,
            "First_name": s.First_name,
            "Last_name": s.Last_name,
            "email": s.email,
            "Phone": s.Phone,
            "dob": s.dob,
            "enrolment_date": s.enrolment_date,
            "status": s.status
        }
        for s in students
    ]
