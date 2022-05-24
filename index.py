from typing import Text
from fastapi import FastAPI, File, UploadFile
from config.db import conn
from models.tb_messages import tb_messages
from schemas.sch_messages import Messages
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import shutil
import document

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>Simple Messanger</h1>
        <h4>Type messages, that you want to save in DB. APIs for messanger you may see in http://127.0.0.1:8000/docs#</h4>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        conn.execute(tb_messages.insert().values(
            message = data
        ))
        await websocket.send_text(f"Message text was: {data}")



# read all data from db
@app.get('/')
def get_all_messages():
    return conn.execute(tb_messages.select()).fetchall()


# read msg by id
@app.get('/{id}')
def get_defined_message(id: int):
    return conn.execute(tb_messages.select().where(tb_messages.c.id == id)).fetchall()


# write new message
@app.post('/')
def write_new_message(sender: str, receiver: str, message: Text, uploaded_file: UploadFile = File(...)): #message: Messages
    url = str("media/" + uploaded_file.filename)
    conn.execute(tb_messages.insert().values(
        sender= sender,
        receiver= receiver,
        message= message,
        url = url,
        # date = tb_messages.date,
    ))

    with open("media/"+ uploaded_file.filename, "wb") as file_object:
        shutil.copyfileobj(uploaded_file.file, file_object)



    return conn.execute(tb_messages.select()).fetchall()


# update data in db
@app.put('/{id}')
def edit_message(id: int, message: Text ): #message: Messages
    conn.execute(tb_messages.update().values(
        message= message,
        # date=tb_messages.date,
    ).where(tb_messages.c.id == id))
    return conn.execute(tb_messages.select()).fetchall()


# delete msg from db
@app.delete('/')
def delete_message(id: int):
    conn.execute(tb_messages.delete().where(tb_messages.c.id == id))
    return conn.execute(tb_messages.select()).fetchall()
