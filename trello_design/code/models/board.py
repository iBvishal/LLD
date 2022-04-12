import uuid
from datetime import datetime
from models.column import Column
from models.enums import BoardStatus
from models.card import Card

from user import User


class Board():

    def __init__(self, name: str, description: str, created_by: User, boardStatus: BoardStatus = BoardStatus.PUBLIC.value) -> None:
        self.id = uuid.uuid1()
        self.name = name
        self.status = boardStatus
        self.created_at = datetime.now()
        self.created_by = created_by
        self.description = description
        self.columns = []

        self.members = []
        self.members.append(created_by)
        self.url = self.get_url()
    
    def get_url(self):
        return "board/" + str(self.id) + "/"
        

