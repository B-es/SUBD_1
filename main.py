from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from api_routes.user_router import user_router
from api_routes.messages_router import messages_router
from api_routes.chats_router import chats_router

app = FastAPI()
app.include_router(user_router, prefix='/users')
app.include_router(messages_router, prefix='/messages')
app.include_router(chats_router, prefix='/chats')

@app.get('/', response_class=HTMLResponse)
async def main_rout() :
    with open('index.html', encoding='utf-8') as f:
        return f.read()


    