# from fastapi import FastAPI
# from config.db import conn
# from models.tb_messages import tb_messages
# from schemas.sch_messages import Messages
#
# routes_messages = FastAPI()
#
#
# #read all data from db
# @routes_messages.get('/')
# def read_data():
#     return conn.execute(tb_messages.select()).fetchall()
#
#
# #read msg by id
# @routes_messages.get('/{id}')
# def read_data(id: int):
#     return conn.execute(tb_messages.select().where(tb_messages.c.id == id)).fetchall()
#
# #write new message
# @routes_messages.post('/')
# def write_data(message: Messages):
#     conn.execute(tb_messages.insert().values(
#         from_whom = tb_messages.from_whom,
#         for_whom = tb_messages.for_whom,
#         message = tb_messages.message,
#        # date = tb_messages.date,
#     ))
#     return conn.execute(tb_messages.select()).fetchall()
#
# #update data in db
# @routes_messages.put('/{id}')
# def update_data(id: int, message: Messages):
#     conn.execute(tb_messages.update(
#         from_whom=tb_messages.from_whom,
#         for_whom=tb_messages.for_whom,
#         message=tb_messages.message,
#        # date=tb_messages.date,
#     ).where(tb_messages.c.id == id))
#     return conn.execute(tb_messages.select()).fetchall()
#
#
# #delete msg from db
# @routes_messages.delete('/')
# def delete_data(id: int):
#     conn.execute(tb_messages.delete().where(tb_messages.c.id == id))
#     return conn.execute(tb_messages.select()).fetchall()