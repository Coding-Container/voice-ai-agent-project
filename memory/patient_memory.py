import json

def get_patient(name):
    with open("database/patients.json") as f:
        data = json.load(f)
    return data.get(name)