from pymongo.collection import Collection
from api_models.User import User
from api_models.Message import Message
from api_models.Chat import Chat
from bson import ObjectId

class CRUD():
    
    def __init__(self, collection: Collection):
        self.collection = collection
        
    def insert(self, obj:User|Message|Chat):
        print("13")
        if(type(obj) is Chat):
            obj.userId1 = ObjectId(obj.userId1)
            obj.userId2 = ObjectId(obj.userId2)
            obj.messages = [ObjectId(messageId) for messageId in  obj.messages]
        return self.collection.insert_one(obj.model_dump())
        
    def select(self) -> list|None:
        return [dict(d) for d in self.collection.find()]
        
    def update(self, obj:User|Message|Chat, newobj:User|Message|Chat):
        return self.collection.update_one(obj.model_dump(), {"$set": newobj.model_dump()})
        
    def delete(self, obj:User|Message|Chat):
        return self.collection.delete_one(obj.model_dump())
        
        
    
        