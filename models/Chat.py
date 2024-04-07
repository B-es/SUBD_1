from dataclasses import dataclass, asdict

from bson import ObjectId

@dataclass
class Chat:
    _id:ObjectId
    userId1:ObjectId
    userId2:ObjectId
    messages:list[ObjectId]
    
    toDict = asdict
    
    def toInsert(self):
        return {
            'userId1': self.userId1,
            'userId2': self.userId2,
            'messages': self.messages,
        }
        
    def fromDict(dict):
        return Chat('', dict['userId1'], dict['userId2'], dict['messages'])