
from pydantic import BaseModel
from typing import  Dict


class Patient(BaseModel):
    
    name: str
    age : int
    weight: float
    married: bool
    allergies: list[str]
    contact_details: Dict[str,str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted into database')
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')
            
patient_info = {'name': 'Pranshu', 'age': 23, 'weight': 68.7, 'married': True,
                'allergies':['pollution','dust'], 'contact_details' :{'email': 'abc@gmail.com', 'phone': '123456789'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)