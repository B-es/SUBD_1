from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from MongoManager import MongoManager
from api_models.Chat import Chat

chats_router = APIRouter()
mongo = MongoManager()
collection = 'chats'
templates = Jinja2Templates(directory="templates/")

@chats_router.get('/select', response_class=HTMLResponse)
def select_route(request: Request):
    res = mongo.get_CRUD(collection).select()
    return templates.TemplateResponse(request=request, name='select.html', context={'count':len(res), 'collection':collection, 'values':res})

@chats_router.delete('/delete')
def delete_route(id:str):
    res =  mongo.get_CRUD(collection).delete(id)
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