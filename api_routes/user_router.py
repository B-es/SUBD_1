from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from MongoManager import MongoManager
from api_models.User import User



user_router = APIRouter()
mongo = MongoManager()
collection = 'users'
templates = Jinja2Templates(directory="templates/")

@user_router.get('/')
def home_route():
    with open('api_routes/html/user.html', encoding='utf-8') as f:
        html_s = f.read()
        return HTMLResponse(html_s)

@user_router.get('/select', response_class=HTMLResponse)
def select_route(request: Request):
    res = mongo.get_CRUD(collection).select()
    return templates.TemplateResponse(request=request, name='select.html', context={'count':len(res), 'collection':collection, 'values':res})

@user_router.delete('/delete')
def delete_route(id:str):
    res =  mongo.get_CRUD(collection).delete(id)
    return res.deleted_count
    
@user_router.put('/update')
def update_route(old:User, new:User):
    res = mongo.get_CRUD(collection).update(old, new)
    return res.modified_count

@user_router.post('/insert')
def insert_route(new:User):
    res = mongo.get_CRUD(collection).insert(new)
    return str(res.inserted_id)