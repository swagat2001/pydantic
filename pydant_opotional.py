from pydantic import BaseModel
from typing import List,Dict,Optional


class Patient(BaseModel):
    
    name:str
    age:int
    weight:float
    married:bool
    allergies:Optional[List[str]] = None # This allows allergies to be optional
    # If allergies are not provided, it defaults to None
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
                'married':False,
                'contact_details':{'email':'abc@gmail.com','phone':'998877'}}
patient1 = Patient(**patient_info)

insert_patient_db(patient1)