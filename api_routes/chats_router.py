from fastapi import APIRouter
from MongoManager import MongoManager
from api_models.Chat import Chat

chats_router = APIRouter()
mongo = MongoManager()
collection = 'chats'

@chats_router.get('/select')
def select_route():
    res = mongo.get_CRUD(collection).select()
    return str(res)

@chats_router.delete('/delete')
def delete_route(toDelete:Chat):
    res =  mongo.get_CRUD(collection).delete(toDelete)
    return res.deleted_count
    
@chats_router.put('/update')
def update_route(old:Chat, new:Chat):
    res = mongo.get_CRUD(collection).update(old, new)
    return res.modified_count

@chats_router.post('/insert')
def insert_route(new:Chat):
    print(new)
    res = mongo.get_CRUD(collection).insert(new)
    return str(res.inserted_id)