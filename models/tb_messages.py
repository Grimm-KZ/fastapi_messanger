import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, Text, DateTime
from config.db import meta
from sqlalchemy_utils import URLType
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
    Column('url', URLType),
    Column('date', DateTime, default=datetime.datetime.now()),
)
