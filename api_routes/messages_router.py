from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from MongoManager import MongoManager
from api_models.Message import Message

messages_router = APIRouter()
mongo = MongoManager()
collection = 'messages'
templates = Jinja2Templates(directory="templates/")

@messages_router.get('/select', response_class=HTMLResponse)
def select_route(request: Request):
    res = mongo.get_CRUD(collection).select()
    return templates.TemplateResponse(request=request, name='select.html', context={'count':len(res), 'collection':collection, 'values':res})

@messages_router.delete('/delete')
def delete_route(id:str):
    res =  mongo.get_CRUD(collection).delete(id)
    return res.deleted_count
    
@messages_router.put('/update')
def update_route(old:Message, new:Message):
    res = mongo.get_CRUD(collection).update(old, new)
    return res.modified_count

@messages_router.post('/insert')
def insert_route(new:Message):
    res = mongo.get_CRUD(collection).insert(new)
    return str(res.inserted_id)