import uuid
from card import Card
from user import User

class Column():

    def __init__(self, name: str, board_id: uuid) -> None:
        self.id = uuid.uuid1()
        self.name = name
        self.board = board_id
        self.cards = []
        self.url = self.get_column_url()
    
    def create_card(self, name: str, description: str = None, user: User = None):
        card = Card(
            name=name,
            description=description,
            user=user,
            column_id=self.id
        )
        self.cards.append(card)

    def delete(self):
        for card in self.cards:
            card.delete()
        super(self).delete()
    
    def show(self):
        for card in self.cards:
            card
    
    def get_column_url(self):
        return "column/" + str(self.id) + "/"
    
    

