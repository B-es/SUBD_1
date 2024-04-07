from dataclasses import dataclass, asdict

from bson import ObjectId

@dataclass
class User:
    _id:ObjectId
    name:str
    surname:str
    age:int
    email:str
    password:str
    
    toDict = asdict
    
    def toInsert(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'email': self.email,
            'password': self.password,
        }

    def fromDict(dict):
        return User('', dict['name'], dict['surname'], dict['age'], dict['email'], dict['password'])
        