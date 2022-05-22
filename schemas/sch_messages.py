from sqlite3 import Date
from pydantic import BaseModel


class Messages(BaseModel):
    sender: str
    receiver: str
    message: str
# date: Date
