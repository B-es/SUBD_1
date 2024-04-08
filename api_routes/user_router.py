from fastapi import APIRouter
from MongoManager import MongoManager
from api_models.User import User

user_router = APIRouter()
mongo = MongoManager()
collection = 'users'

@user_router.get('/select')
def select_route():
    res = mongo.get_CRUD(collection).select()
    return str(res)

@user_router.delete('/delete')
def delete_route(toDelete:User):
    res =  mongo.get_CRUD(collection).delete(toDelete)
    return res.deleted_count
    
@user_router.put('/update')
def update_route(old:User, new:User):
    res = mongo.get_CRUD(collection).update(old, new)
    return res.modified_count

@user_router.post('/insert')
def insert_route(new:User):
    res = mongo.get_CRUD(collection).insert(new)
    return str(res.inserted_id)