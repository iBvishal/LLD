import uuid
from datetime import datetime
from column import Column
from enums import BoardStatus
from card import Card

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
        self.url = self.get_board_url()
    
    def update_board(self, name: str = None, description: str = None, boardStatus: BoardStatus = None):
        self.name = name if not name is None else self.name
        self.description = description if not description is None else self.description
        self.boardStatus = boardStatus if not boardStatus is None else self.boardStatus

    def create_column(self, name: str):
        column = Column(
            name=name,
            board_id = self.id 
        )
        self.columns.append(column)
    
    def move_card(self, card: Card, form_column: Column, to_column: Column):
        form_column.cards.remove(card)
        to_column.add(card)

    def add_member(self, user: User):
        self.members.append(user)
    
    def remove_member(self, user: User):
        if user is not self.created_by:
            self.members.remove(user)
        
    def delete(self):
        for column in self.columns:
            column.delete()
        del self
    
    def get_board_url(self):
        return "board/" + str(self.id) + "/"
        

