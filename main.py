import json

from fastapi import FastAPI, Path

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data
@app.get("/")
def hello() :
    return {'message': 'Patient management system API'}

@app.get('/about')
def about():
    return {'message':  'this is the second test of /about address from API'}


@app.get('/view')
def view():
    data = load_data()
    
    return data
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description = 'ID of thr patient in the DB', example = 'P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {'error':'patient_id not found'}