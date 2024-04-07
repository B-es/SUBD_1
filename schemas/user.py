users_schema = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "surname", "age", "email", "password"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "surname": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "age": {
                    "bsonType": "int",
                    "description": "must be an integer greater than 14 and",
                    "minimum": 14
                },
                "email": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "password": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "chats": {
                    "bsonType": "array",
                    "description": "must be an array and is required",
                    "items": {
                        "bsonType": "objectId",
                        "description": "must be an objectId and is required"
                    },
                    "minItems": 1,
                },
            }
        }
    }



