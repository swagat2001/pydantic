from pydantic import BaseModel
from typing import List,Dict


class Patient(BaseModel):
    
    name:str
    age:int
    weight:float
    married:bool
    allergies:List[str]  # This validate that the entries are in this is string store as a list
    contact_details:Dict[str,str]
    

def insert_patient_db(patient:Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    
def update_patient_db(patient:Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    
    
patient_info = {'name':'Swagat','age':24,'weight':65,
                'married':False,'allergies':['dust'],
                'contact_details':{'email':'abc@gmail.com','phone':'998877'}}
patient1 = Patient(**patient_info)

insert_patient_db(patient1)