
#Field - to attach additional validation and metadata to model fields.
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict, Optional

class Patient(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    email:EmailStr
    age: int= Field(gt=0)
    weight:float = Field(gt=0)
    married:bool
    allergies:Optional[List[str]]=Field(max_length=5)
    contact_details:Dict[str,str]



def update_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print(patient.email)
        print('updated')

patient_info = {'name': 'John Doe', 'email': 'john.doe@example.com', 'age': 30, 'weight': 70.5, 'married': True, 
    'allergies': ['penicillin'], 'contact_details': {'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
