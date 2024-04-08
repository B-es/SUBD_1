from fastapi import APIRouter
from MongoManager import MongoManager
from api_models.Message import Message

messages_router = APIRouter()
mongo = MongoManager()
collection = 'messages'

@messages_router.get('/select')
def select_route():
    res = mongo.get_CRUD(collection).select()
    return str(res)

@messages_router.delete('/delete')
def delete_route(toDelete:Message):
    res =  mongo.get_CRUD(collection).delete(toDelete)
    return res.deleted_count
    
@messages_router.put('/update')
def update_route(old:Message, new:Message):
    res = mongo.get_CRUD(collection).update(old, new)
    return res.modified_count

@messages_router.post('/insert')
def insert_route(new:Message):
    res = mongo.get_CRUD(collection).insert(new)
    return str(res.inserted_id)