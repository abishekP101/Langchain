from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel):
    name: str = 'abishek'
    age: Optional[int] = None
    cgpa: float= Field(gt=0 , lt=10 , default=5 , description='A decimal value representing academic score')

new_student = {'age': '32' , 'cgpa':9}
student = Student(**new_student)
student_dict = dict(student)


print(student_dict['age'])