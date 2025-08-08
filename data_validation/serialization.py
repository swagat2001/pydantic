from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address
    
address_dict = {'city': 'Balasore','state':'odisha','pin':'756001'}
address1 = Address(**address_dict)

patient_dict = {'name': 'Swagat', 'gender':'male','age': 24, 'address': address1}
patient1 = Patient(**patient_dict)

temp = patient1.model_dump()  # This will print the model in a dictionary format
print(temp)
type(temp)  # This will show the type of the variable temp  


json_data = patient1.model_dump_json()  # This will convert the model to JSON format
print(json_data)