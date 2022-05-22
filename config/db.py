from sqlalchemy import create_engine, MetaData


engine = create_engine(
    "sqlite:///./msg.sqlite3",
     connect_args= {'check_same_thread': False},
)

meta = MetaData()
conn = engine.connect()