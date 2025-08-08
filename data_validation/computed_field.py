from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict


class Patient(BaseModel):
    
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]  # This validate that the entries are in this is string store as a list
    contact_details:Dict[str,str]
    
    @computed_field
    @property
    
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.age ** 2),2)  # Simplified BMI calculation for demonstration
        return bmi
    

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
    print('BMI',patient.calculate_bmi)
    print(patient.contact_details)
    
    
patient_info = {'name':'Swagat','email':'abc@gmail.com','age':24,'weight':65,'height':1.75,
                'married':False,'allergies':['dust'],
                'contact_details':{'phone':'998877'}}
patient1 = Patient(**patient_info)

update_patient_db(patient1)