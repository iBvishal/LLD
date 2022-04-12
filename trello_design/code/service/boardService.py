from models.enums import BoardStatus
from interface import basicInterface
from cardService import CardService
from columnService import ColumnService

class BoardService(basicInterface):

    def __init__(self) -> None:
        self.column_service = ColumnService()
        self.card_service = CardService()

    def create(self, ):
        pass

    def update(self, ):
        pass

    def delete(self, ):
        pass

    def create_column(self, ):
        pass
    
    def move_card(self, ):
        pass

    def add_member_to_board(self, ):
        pass
    
    def remove_member_to_board(self, ):
        pass