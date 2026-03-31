from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException, status
import logging

logger = logging.getLogger("students-crud")

def get_all_students(db: Session):
    logger.info("Obteniendo informacion de todos los estudiantes")
    return db.query(models.Student).all()

def get_student_by_id(db: Session, student_id: int):
    logger.info(f"Buscando estudiante id={student_id}")
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        logger.warning(f"Estudiante id={student_id} no existe")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="student not found")
    return student

def create_student(db: Session, student_in: schemas.StudentCreate):
    logger.info(f"Creando el email={student_in.email} para el estudiante")
    existing = db.query(models.Student).filter(models.Student.email == student_in.email).first()
    if existing:
        logger.error(f"El email {student_in.email} ya existe")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="email already exists")
    student = models.Student(name=student_in.name, email=student_in.email, master=student_in.master)
    db.add(student)
    db.commit()
    db.refresh(student)
    logger.info(f"Estudiante creado id={student.id} correctamente")
    return student

def delete_student(db: Session, student_id: int):
    logger.info(f"Eliminando estudiante id={student_id}")
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        logger.warning(f"Estudiante id={student_id} no existe")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="student not found")
    db.delete(student)
    db.commit()
    logger.info(f"Estudiante id={student_id} ha sido eliminado con exito!!!")
    return