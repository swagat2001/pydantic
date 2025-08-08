from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict


class Patient(BaseModel):
    
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]  # This validate that the entries are in this is string store as a list
    contact_details:Dict[str,str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients over 60 must have an emergency contact.") 
        return
    

def insert_patient_db(patient:Patient):
    
    print(patient.name)
    print(patient.email)
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
    
    
patient_info = {'name':'Swagat','email':'abc@gmail.com','age':24,'weight':65,
                'married':False,'allergies':['dust'],
                'contact_details':{'phone':'998877'}}
patient1 = Patient(**patient_info)

insert_patient_db(patient1)