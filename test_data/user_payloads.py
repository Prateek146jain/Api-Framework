import random

def create_user_payload():
    return {
        "name": "Tester",
        "gender": "Male",
        "email": f"Prateek{random.randint(111,999)}@gmail.com",
        "status": "Active"
    }

def update_user_payload():
    return {
        "name": "Jainwpkj",
        "email": f"jain{random.randint(1111,9999)}@gmail.com",
        "status": "active"
    }


def create_user_payload_blank():
    return {
        "name": "",
        "gender": "",
        "email": "",
        "status": ""
    }
