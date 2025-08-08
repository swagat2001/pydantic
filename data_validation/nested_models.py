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

patient_info = {'name': 'Swagat', 'gender':'male','age': 24, 'address': address1}
patient1 = Patient(**patient_info)

print(patient1)