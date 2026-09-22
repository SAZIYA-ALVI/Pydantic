
from pydantic import BaseModel,EmailStr,model_validator,field_validator
from typing import List,Dict

class Patient(BaseModel):
    name: str
    age: int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

@field_validator('email')
@classmethod
def email_validator(cls, value):
      valid_domains = ['hdfc.com', 'icici.com']
      #abc@gmal.com
      domain_name = value.split('@')[-1]

      if domain_name not in valid_domains:
            raise valueError('Not a valid domain')
      return value

      @field_validator('name')
      @classmethod
      def transform_name(cls, value):
            return value.upper()

      @field_validator('age')
      @classmethod
      def validate_age(cls, value):
            if 0<value < 100:
                 return value
            else:
                  raise ValueError('Age should be in between 0 and 100')


def update_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('updated')

patient_info = {'name': 'John Doe', 'email': 'john@hdfc.com', 'age': 30, 'weight': 70.5, 'married': True,
         'allergies': ['penicillin'], 'contact_details': {'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)# validation will be performed here, and if the email domain is not valid, a ValueError will be raised.
update_patient_data(patient1)
