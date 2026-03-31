import logging
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, BVase, get_db

# Crear las tablas en la base de datos 
Base.metadata.create_all(bind=engine)

# Logging basico
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger("students-opi")

app = FastAPI(title="Students CRUD API")

@app.get("/students", response_model=list[schemas.Student])
def list_students(db: Session = Depends(get_db)):
    return crud.get_all_students(db)

@app.post("/students", response_model=schemas.Student, status_code=status.HTTP_201_CREATED)
def create_student(student_in: schemas.StudentCreate, db: Session = Depends(get_db)):
    # Pydantic ya valida tipos; aqui delegamos a crud para validaciones de negocio
    return crud.create_student(db, student_in)

@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_student(student_id: int, db: Session = Depends(get_db)):
    crud.delete_student(db, student_id)
    return None