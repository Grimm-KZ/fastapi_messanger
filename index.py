from fastapi import FastAPI
from config.db import conn
from models.tb_messages import tb_messages
from schemas.sch_messages import Messages

app = FastAPI()


# read all data from db
@app.get('/')
def read_data():
    return conn.execute(tb_messages.select()).fetchall()


# read msg by id
@app.get('/{id}')
def read_data(id: int):
    return conn.execute(tb_messages.select().where(tb_messages.c.id == id)).fetchall()


# write new message
@app.post('/')
def write_data(message: Messages):
    conn.execute(tb_messages.insert().values(
        sender=tb_messages.c.sender,
        receiver=tb_messages.c.receiver,
        message=tb_messages.c.message,
        # date = tb_messages.date,
    ))
    return conn.execute(tb_messages.select()).fetchall()


# update data in db
@app.put('/{id}')
def update_data(id: int, tb_message: Messages):
    conn.execute(tb_messages.update(
        sender=tb_messages.c.sender,
        receiver=tb_messages.c.receiver,
        message=tb_messages.c.message,
        # date=tb_messages.date,
    ).where(tb_messages.c.id == id))
    return conn.execute(tb_messages.select()).fetchall()


# delete msg from db
@app.delete('/')
def delete_data(id: int):
    conn.execute(tb_messages.delete().where(tb_messages.c.id == id))
    return conn.execute(tb_messages.select()).fetchall()
