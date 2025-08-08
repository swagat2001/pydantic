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

** Field validator **











