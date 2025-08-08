from pydantic import BaseModel


class Patient(BaseModel):
    name : str
    age : int
    
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
    
def insert_db(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')
patient_info = {'name' : 'Swagat', 'age' : 30}
patient1 = Patient(**patient_info)

insert_db(patient1)