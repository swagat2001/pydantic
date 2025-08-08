from pydantic import BaseModel,EmailStr
from typing import List,Dict

class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    Weight : float
    married:bool
    allergies:List[str]
    contact_details: Dict[str,str]
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.Weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
        
patient_info = {
    'name': 'Swagat','email':'swag@gmail.com','age': 24,
    'Weight': 65, 'married': False, 'allergies': ['dust'],
    'contact_details': {'phone': '998877'}}
    
patient1 = Patient(**patient_info)
insert_patient_data(patient1)
    