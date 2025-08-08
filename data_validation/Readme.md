- Pydantic provide us some custome data types that we can use to validate our data. May be the data is not python data type but we can use Pydantic to validate it.
- Pydantic's `Field` function allows us to set constraints on model fields, such as minimum and maximum values, default values, and more.
- Pydantic's `validator` decorator allows us to define custom validation logic for model fields
- Pydantic's `BaseModel` allows us to define models with type annotations, which can be used to validate data structures.
- Pydantic supports complex data types such as lists, dictionaries, and nested models.
- Pydantic provide builtin data type to validate email, url, and other common data types.
# **Field:**
- Pydantic use `Field` for specific data validation according to the required use case.

```python
from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import Dict



class Patient(BaseModel):
    
    name : str
    email :EmailStr
    Linkdin_URL : AnyUrl
    age : int
    weight : float = Field(gt=0)
    contact_details : Dict[str,str]

# rest code
```  

- Field function also use to attach metadata to the field, such as a description or example value. So that the programmer understand what the function is doing.
- Useful at building API documentation, as it provides additional context for each field.

# ** Field validator **
- field validator is used to validate the data of a specific field in a Pydantic model.
- It allows us to define custom validation logic for a specific field in a Pydantic model.
```python

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

# rest code
```
- It is used to validate the data of a specific field in a Pydantic model.
- It allows us to define custom validation logic for a specific field in a Pydantic model.

# **Model validator**

- Model validator is used to validate the data of the entire Pydantic model.
- It allows us to define custom validation logic for the entire Pydantic model.

```python
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
    
    # below we are using model_validator to validate the entire model
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
    
    
patient_info = {'name':'Swagat','email':'abc@gmail.com','age':61,'weight':65,
                'married':False,'allergies':['dust'],
                'contact_details':{'phone':'998877', 'emergency':'999947475'}}
patient1 = Patient(**patient_info)

insert_patient_db(patient1)
```

# **Computed_fields:**
- Pydantic allows us to define computed fields, which are fields that are derived from other fields in the model.









