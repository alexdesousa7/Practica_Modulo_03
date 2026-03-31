from pydantic import BaseModel, EmailStr, constr

class StudentBase(BaseModel):
    name: constr(min_length=1)
    email: EmailStr
    master: constr(min_length=1)

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True