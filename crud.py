#create,read, update, delete
from sqlalchemy.orm import Session
from model import Student
from input_model import StudentInput

def get_student(db: Session, skip: int=0,limit:int=100):
    return db.query(Student).offset(skip).limit(limit).all()

def get_student_by_id(db:Session,student_id:int):
    return db.query(Student).filter(Student.id==student_id).first()

def create_student_profile(db:Session, student_var: StudentInput):
    _student = Student(id=student_var.id,name=student_var.name)
    db.add(_student)
    db.commit()
    db.refresh(_student)
    return _student

def remove_student(db:Session,student_id:int):
    _student=get_student_by_id(db=db, student_id=student_id)
    db.delete(_student)
    db.commit()

def update_student(db:Session,student_id:int,name:str):
    _student=get_student_by_id(db=db,student_id=student_id)
    _student.id=student_id
    _student.name=name
    db.commit()
    db.refresh(_student)
    return _student