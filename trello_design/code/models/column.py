import uuid
from models.card import Card
from models.user import UserModel

class Column():

    def __init__(self, name: str, board_id: uuid) -> None:
        self.id = uuid.uuid1()
        self.name = name
        self.board = board_id
        self.cards = []
        self.url = self.get_url()
    
    def get_url(self):
        return "column/" + str(self.id) + "/"
    
    

