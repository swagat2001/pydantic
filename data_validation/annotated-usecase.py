from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import Dict,Annotated,Optional,List



class Patient(BaseModel):
    
    name : Annotated[str, Field(max_length=50,title="Patient Name", description="Ensure name is not too long than 50 characters",examples=["Swagat Mohanty"])]  
    email :EmailStr
    Linkdin_URL : AnyUrl
    age : int = Field(gt=0,lt=120)  # Ensure age is greater than 0
    weight : float = Field(gt=0)  # Ensure weight is greater than 0
    # Adding a field description for clarity)
    married:Annotated[bool, Field(default=None, description="Is the patient is married or not")]
    allergies:Optional[List[str]] = Field(max_length=5)  # Ensure allergies list does not exceed 5 items
    # Adding a field description for clarity
    contact_details : Dict[str,str]


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.Linkdin_URL)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    
    
patient_info = {'name':'Swagat','email':'swagat@gmail.com','Linkdin_URL':'http://linkedin.com/123'
                ,'age': 24,'weight':65,'allergies': ['dust', 'pollen'],
                'contact_details':{'phone':'998877'}}
patient1 = Patient(**patient_info)
update_patient_data(patient1)