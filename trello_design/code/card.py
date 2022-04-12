from enums import CardStatus
from user import User
import uuid

class Card():
    def __init__(self, name: str, description: str, user: User, column_id: uuid) -> None:
        self.id = uuid.uuid1()
        self.name = name
        self.description = description
        self.column_id = column_id
        self.status = CardStatus.TODO.value
        self.url = self.get_card_url()

        self.user = user
    
    def update(self, name: str, description: str = None, user: User = None, new_column: uuid = None):
        self.name = name if not name is None else self.name
        self.description = description if not description is None else self.description
        self.user = user if not user is None else self.user
        
        if not new_column is None:
            self.update_column(new_column)
    
    def update_column(self, new_column: uuid):
        old_column = self.column
        self.column = new_column

        self.url = self.get_card_url()

        old_column.cards.remove(self)
        new_column.cards.add(self)

    def delete(self):
        super(self).delete()

    def get_card_url(self):
        return "card/" + str(self.id) + "/"

    def __repr__(self):
        return f'(name={self.name},\n description={self.description},\n  user={self.user.name}, \n Column={self.column.name})'
