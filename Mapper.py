from bson import ObjectId
from models.User import User
from models.Message import Message
from models.Chat import Chat

class Mapper:
    def toModel(obj_list:list[dict]):
        if not obj_list: return []
        models = []
        
        type = 3
        if obj_list[0].get('name', False): type = 1
        if obj_list[0].get('date', False): type = 2
        
        
        for obj in obj_list:

            if type == 1:   
                model = User(ObjectId(obj['_id']), obj['name'], obj['surname'], obj['age'], obj['email'], obj['password'])
            elif type == 2:
                model = Message(ObjectId(obj['_id']), obj['message'], obj['date'])
            else:
                messages = [ObjectId(id) for id in obj['messages']]     
                model = Chat(ObjectId(obj['_id']), ObjectId(obj['userId1']), ObjectId(obj['userId2']), messages)
            models.append(model)
        return models