from pymongo import MongoClient
from CRUD import CRUD
from schemas.user import users_schema
from schemas.chat import chats_schema
from schemas.message import messages_schema
from generate.generator import create_users, create_chats, create_messages, get_random_chats

class MongoManager:
    
    def __init__(self, uri="mongodb://localhost:27017", dbname = "SUBD1"):
        self.mongo = MongoClient(uri)
        self.uri = uri
        self.db = self.mongo.get_database(dbname)
        self.users_crud = CRUD(self.db.users)
        self.messages_crud = CRUD(self.db.messages)
        self.chats_crud = CRUD(self.db.chats)
        
    def get_CRUD(self, collection:str):
        match collection:
            case 'users':
                return self.users_crud
            case 'messages':
                return self.messages_crud
            case 'chats':
                return self.chats_crud    
        
    def create_collection(self, collection_name:str, validator):
        try:
            self.db.create_collection(collection_name)
        except Exception as e:
            print(e)
        self.db.command("collMod", collection_name, validator=validator)
        
    def create_and_fills_collections(self, count = 10):
        if not self.db.list_collection_names():
            #Создаём коллекции
            for name, validator in zip(["users", "chats", "messages"], [users_schema, chats_schema, messages_schema]):
                self.create_collection(name, validator)
                
            #Создаём индекс на имя для коллекций user, chat и message
            self.db.users.create_index("name")
            self.db.chats.create_index("_id")
            self.db.messages.create_index("_id")

            print("Коллекции созданы")

        if self.db.users.find_one() == None:
            users_data = create_users(count) 
            messages_data = create_messages(count)

            users_ids = self.db.users.insert_many(users_data).inserted_ids
            messages_ids = self.db.messages.insert_many(messages_data).inserted_ids
            
            chats_data = create_chats(count, users_ids, messages_ids)
            chats_ids = self.db.chats.insert_many(chats_data).inserted_ids
            
            chats_parts = get_random_chats(count, chats_ids)
            
            for user_id, chat_part in zip(users_ids, chats_parts):
                self.db.users.update_one({"_id":user_id}, {"$set": {"chats":chat_part}})
            print("Данные залиты")

    def test_output(self):
        user = self.db.users.find_one()
        chat = self.db.chats.find_one({"_id": user['chats'][0]})

        for message_id in chat['messages']:
            document = self.db.messages.find_one({"_id":message_id})
            message = document['message']
            date = document['date']
            print(f"Message: {message}\nDate: {date}")
            
    