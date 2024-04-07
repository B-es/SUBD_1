from bson import ObjectId
from fastapi.responses import HTMLResponse
from MongoManager import MongoManager
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

import ast

mongo = MongoManager()

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get('/', response_class=HTMLResponse)
async def main_rout() :
    return '''
<html>
<head>
<title>Главная страница</title>
</head>
<body style="background-color: rgb(17, 17, 17);color:white">
<h1>Коллекции: user, messages, chats</h1>
<h1>CRUD: select, delete, update, insert</h1>
<h1>q=параметр, для update q1, q2 - соответственно старый и новый записи</h1>
<h1>Пример: /коллекция/crud?q=\{\}</h1>
</body>
</html>
'''

@app.get('/{collection}/select')
def select_route(request:Request, collection:str, q=None):
    obj = ast.literal_eval(q) if q != None else {}
    if obj.get('_id'): obj['_id'] = ObjectId(obj['_id'])
    values = mongo.get_CRUD(collection).select(obj)
    context = {'request':request,'action':'select', 'collection': collection, 'values': values, 'count': len(values)}
    return templates.TemplateResponse(name='select.html',context=context)

@app.get('/{collection}/delete')
def delete_route(request:Request, collection:str, q=None):
    obj = ast.literal_eval(q) if q != None else {}
    if obj.get('_id'): obj['_id'] = ObjectId(obj['_id'])
    values = mongo.get_CRUD(collection).delete(obj)
    context = {'request':request,'action':'delete', 'collection': collection, 'result': values.deleted_count}
    return templates.TemplateResponse(name='common.html',context=context)

@app.get('/{collection}/update')
def delete_route(request:Request, collection:str, q1=None, q2=None):
    obj = ast.literal_eval(q1) if q1 != None else {}
    newobj = ast.literal_eval(q2) if q2 != None else {}
    if obj.get('_id'): obj['_id'] = ObjectId(obj['_id'])
    if newobj.get('_id'): newobj['_id'] = ObjectId(newobj['_id'])
    values = mongo.get_CRUD(collection).update(obj, newobj)
    context = {'request':request,'action':'update', 'collection': collection, 'result': values.modified_count}
    return templates.TemplateResponse(name='common.html',context=context)

@app.get('/{collection}/insert')
def delete_route(request:Request, collection:str, q=None):
    obj = ast.literal_eval(q) if q != None else {}
    values = mongo.get_CRUD(collection).insert(obj)
    context = {'request':request,'action':'insert', 'collection': collection, 'result': values.inserted_id}
    return templates.TemplateResponse(name='common.html',context=context)