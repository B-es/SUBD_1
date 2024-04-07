messages_schema = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["message", "date"],
            "properties": {
                "message": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "date": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
            }
        }
    }



