from dataclasses import dataclass, asdict

from bson import ObjectId

@dataclass
class Message:
    _id:ObjectId
    message:str
    date:str
    
    toDict = asdict
    
    def toInsert(self):
        return {
            'message': self.message,
            'date': self.date,
        }
        
    def fromDict(dict):
        return Message('', dict['message'],  dict['date'])