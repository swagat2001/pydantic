from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import Dict



class Patient(BaseModel):
    
    name : str = Field(max_length=50) # Ensure name is not too long than 50 characters
    email :EmailStr
    Linkdin_URL : AnyUrl
    age : int = Field(gt=0,lt=120)  # Ensure age is greater than 0
    weight : float = Field(gt=0)  # Ensure weight is greater than 0
    # Adding a field description for clarity)
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