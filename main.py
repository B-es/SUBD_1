from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from api_routes.user_router import user_router
from api_routes.messages_router import messages_router
from api_routes.chats_router import chats_router

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
app.include_router(user_router, prefix='/users')
app.include_router(messages_router, prefix='/messages')
app.include_router(chats_router, prefix='/chats')

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
</body>
</html>
'''


    