from pydantic import BaseModel,EmailStr,field_validator
from typing import List,Dict


class Patient(BaseModel):
    
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]  # This validate that the entries are in this is string store as a list
    contact_details:Dict[str,str]
    
    
    # if the email is allowed for specific domain only then we can use field_validator as below
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domain = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domain:
            raise ValueError(f"{domain_name} is Not a valid domain")
        return value
    
    # Again Now we want that the name should be always in uppercase
    @field_validator('name')
    @classmethod
    
    def name_validator(cls, value):
        return value.upper()

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
    
    
patient_info = {'name':'Swagat','email':'abc@hdfc.com','age':24,'weight':65,
                'married':False,'allergies':['dust'],
                'contact_details':{'phone':'998877'}}
patient1 = Patient(**patient_info)

insert_patient_db(patient1)