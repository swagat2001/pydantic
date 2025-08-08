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









