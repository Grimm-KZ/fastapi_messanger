from typing import Text
from fastapi import FastAPI, File, UploadFile
from config.db import conn
from models.tb_messages import tb_messages
from schemas.sch_messages import Messages
import shutil


app = FastAPI()


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
