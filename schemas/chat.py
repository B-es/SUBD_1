chats_schema = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["userId1", "userId2", "messages"],
            "properties": {
                "userId1": {
                    "bsonType": "objectId",
                    "description": "must be a objectId and is required"
                },
                "userId2": {
                    "bsonType": "objectId",
                    "description": "must be a objectId and is required"
                },
                "messages": {
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
