from bson import ObjectId
from pymongo.collection import Collection
from Mapper import Mapper
from models.User import User
from models.Message import Message
from models.Chat import Chat


class CRUD():
    
    def __init__(self, collection: Collection):
        self.collection = collection
        
    def insert(self, obj:User|Message|Chat|dict):
        if(type(obj) is dict):
            if(self.collection.name == 'users'):
                obj = User.fromDict(obj)
            elif(self.collection.name == 'messages'):
                obj = Message.fromDict(obj)
            else:
                obj = Chat.fromDict(obj)
        return self.collection.insert_one(obj.toInsert())
        
    def select(self, obj:dict = None) -> list|None:
        return Mapper.toModel(list(self.collection.find(obj)))
        
    def update(self, obj:User|Message|Chat|dict, newobj:User|Message|Chat|dict):
        if(type(obj) is dict): 
            return self.collection.update_one(obj, {"$set": newobj})
        else: return self.collection.update_one(obj.toDict(), {"$set": newobj.toDict()})
        
    def delete(self, obj:User|Message|Chat|dict):
        if(type(obj) is dict): return self.collection.delete_one(obj)
        else: return self.collection.delete_one(obj.toDict())
        
        
    
        