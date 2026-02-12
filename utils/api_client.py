import requests


def get_user(url, headers):
    return requests.get(url, headers=headers)

def create_user(url, payload, headers):
    return requests.post(url, json=payload, headers=headers)

# def get_user(url, headers):
#     return requests.get(url, headers=headers)

def update_user_details(url, payload, headers):
    return requests.put(url, json=payload, headers=headers)

def delete_user(url, headers):
    return requests.delete(url, headers=headers)
