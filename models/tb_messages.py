from sqlalchemy import MetaData, Table, Column, Integer, String, Text, Date
from config.db import meta
import sqlalchemy as sa


tb_messages = Table(
    'tb_messages', meta,
    #id = sa.Column(sa.Integer, primary_key=True),
   # from_whom = sa.Column(sa.String),
   # for_whom = sa.Column(sa.String),
   # message = sa.Column(sa.String),
    Column('id', Integer, primary_key=True),
    Column('sender', String(255)),
    Column('receiver', String(255)),
    Column('message', Text),
    # Column('date', Date),
)
