from pydantic import BaseModel,EmailStr,AnyUrl
from typing import Dict



class Patient(BaseModel):
    
    name : str
    email :EmailStr
    Linkdin_URL : AnyUrl
    age : int
    weight : float
    contact_details : Dict[str,str]


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.Linkdin_URL)
    print(patient.weight)
    print(patient.contact_details)
    
    
patient_info = {'name':'Swagat','email':'swagat@gmail.com','Linkdin_URL':'http://linkedin.com/123'
                ,'age': 24,'weight':65,
                'contact_details':{'phone':'998877'}}
patient1 = Patient(**patient_info)
update_patient_data(patient1)