
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Dict, Optional, Annotated
from typing import List


class Patient(BaseModel):
    
    name: Annotated[str, Field(max_length = 50, title = 'name of the patient', description = 'give the name of the patient in less than 50 chars', examples =['aman','Harsh'])]
    age : int = Field(gt=0, lt=120)
    email: EmailStr
    linkedin_url : AnyUrl
    weight: Annotated[float, Field(gt=0, strict = True, description = 'weight of the patient in kg')]
    married: Annotated[bool, Field(default=None, description='is the patient married or not')]
    allergies: Annotated[Optional[list[str]], Field(default = None,max_length = 5)]
    contact_details: Dict[str,str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.linkedin_url)
    print(patient.allergies)
    print('Inserted into database')
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')
            
patient_info = {'name': 'Pranshu', 'age': 23, 'email': 'abc@gmail.com', 'linkedin_url' : 'https://linkedin/001', 'weight': 68.7, 'married': True,
                'contact_details' :{'phone': '123456789'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)