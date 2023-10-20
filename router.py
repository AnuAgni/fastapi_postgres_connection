from fastapi import APIRouter,HTTPException,Path,Depends
from database import sessionLocal
from sqlalchemy.orm import Session
from input_model import StudentInput,RequestStudent,Response
import crud

router=APIRouter()
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create(request:RequestStudent, db: Session=Depends(get_db)):
    crud.create_student_profile(db,request.parameter)
    return Response(code=200,status="ok",message="created").dict(exclude_none=True)

@router.get("/")
async def get(db:Session=Depends(get_db)):
    _student=crud.get_student(db,0,100)
    return Response(code=200,status="ok",message="fetch all").dict(exclude_none=True)

@router.get("/{id}")
async def get_by_id(id:int,db:Session=Depends(get_db)):
    _student = crud.get_student_by_id(db,id)
    return Response(code=200,status="ok",message="student is").dict(exclude_none=True)

@router.post("/update")
async def update_student(request: RequestStudent,db:Session=Depends(get_db)):
    _student=crud.update_student(db,book_id=request.parameter.id,name=request.parameter.name)
    return Response(code=200,status="ok",message="updated").dict(exclude_none=True)

@router.delete("/{id}")
async def delete(id:int,db:Session=Depends(get_db)):
    crud.remove_student(db, student_id=id)
    return Response(code=200,status="ok",message="deleted").dict(exclude_none=True)