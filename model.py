#table for postgresql
from sqlalchemy import Column, String,Integer
from database import base

class Student(base):
    __tablename__='student'
    id=Column(Integer,primary_key=True)
    name=Column(String)
