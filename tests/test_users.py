from config.config import baseurl, headers
from test_data.user_payloads import create_user_payload, update_user_payload,create_user_payload_blank
from utils.api_client import create_user, get_user, update_user_details,delete_user
from Schema.schema import create_user_schema
from jsonschema import validate

User_id = None

def test_create_new_user():  # Create a new user with all valid values
    global User_id
    res = create_user(baseurl, create_user_payload(), headers)
    assert res.status_code == 201
    assert res.json()["name"]=="Tester"
    assert res.json()["status"]=="active"
    User_id = res.json()["id"]

def test_create_user_missing_name(): # Try to create a new user without entering the name.
    payload = create_user_payload()
    payload.pop("name")
    res = create_user(baseurl, payload, headers)
    assert res.status_code == 422

def test_create_user_missing_email(): #try to create a new user without entering the email
    payload = create_user_payload()
    payload.pop("email")
    res = create_user(baseurl, payload, headers)
    assert res.status_code == 422

def test_create_user_missing_status(): # try to create a new user without entering the status
    payload = create_user_payload()
    payload.pop("status")
    res = create_user(baseurl, payload, headers)
    assert res.status_code == 422,'Assertion failed due to missing required field'


def test_create_user_missing_all_fields():
    payload = create_user_payload_blank()
    res = create_user(baseurl, payload, headers)
    assert res.status_code == 422 ,'Error Email field is required'

def test_get_user_details():
    res = get_user(f"{baseurl}/{User_id}", headers)
    assert res.status_code == 200
    assert res.json()["name"]=="Tester"
    assert res.json()["status"]=="active"
    assert res.json()["id"]==User_id
    validate(instance=res.json(), schema=create_user_schema)



def test_update_user_details():
    res = update_user_details(f"{baseurl}/{User_id}", update_user_payload(), headers)
    assert res.status_code == 200
    assert res.json()["name"]=="Jainwpkj"
    assert res.json()["status"]=="active"
    assert res.json()["id"]==User_id


def test_get_user_details_check():
    res = get_user(f"{baseurl}/{User_id}", headers)
    assert res.status_code == 200
    assert res.json()["id"]==User_id

def test_delete_user():
    res = delete_user(f"{baseurl}/{User_id}", headers)
    assert res.status_code == 204


