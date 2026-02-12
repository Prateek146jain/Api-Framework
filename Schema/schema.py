import jsonschema


create_user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "gender": {"type": "string"},
        "status": {"type": "string"}
    },
    "required": ["id", "name", "email", "gender", "status"]
}

print(type(create_user_schema))