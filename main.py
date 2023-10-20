from fastapi import FastAPI
import model
from database import engine
import router

model.base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
async def root():
    return "Hello"

app.include_router(router.router,prefix="/book",tags=["book"])