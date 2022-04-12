from interface import basicInterface
from cardService import CardService
from models.user import UserModel

class ColumnService(basicInterface):
    def __init__(self) -> None:
        self.card_service = CardService()

    def create(self, ):
        pass

    def update(self, ):
        pass
    
    def delete(self):
        pass