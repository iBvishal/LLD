from models.enums import CardStatus
from models.user import UserModel
import uuid

class Card():
    def __init__(self, name: str, description: str, user: UserModel, column_id: uuid) -> None:
        self.id = uuid.uuid1()
        self.name = name
        self.description = description
        self.column_id = column_id
        self.status = CardStatus.TODO.value
        self.url = self.get_url()

        self.user = user

    def delete(self):
        super(self).delete()

    def get_url(self):
        return "card/" + str(self.id) + "/"

    def __repr__(self):
        return f'(name={self.name},\n description={self.description},\n  user={self.user.name}, \n Column={self.column.name})'
