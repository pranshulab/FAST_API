
from pydantic import BaseModel, EmailStr, AnyUrl
from typing import Dict, Optional
from typing import List


class Patient(BaseModel):
    
    name: str
    age : int
    # email: EmailStr
    linkedin_url : AnyUrl
    weight: float
    married: bool
    allergies: Optional[list[str]] = None
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
            
patient_info = {'name': 'Pranshu', 'age': 23, 'linkedin_url' : 'https://linkedin/001', 'weight': 68.7, 'married': True,
                'contact_details' :{'phone': '123456789'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)