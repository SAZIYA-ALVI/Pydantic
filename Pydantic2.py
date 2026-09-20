
from pydantic import BaseModel
from typing import List,Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight:float
    married:bool
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]

"""def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')"""

def update_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('updated')

patient_info = {'name': 'John Doe', 'email': 'john.doe@example.com', 'age': 30, 'weight': 70.5, 'married': True,
         'allergies': ['penicillin'], 'contact_details': {'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
