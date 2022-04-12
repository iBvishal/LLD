import email
import uuid

class User():

    def __init__(self, name: str, email: email) -> None:
        self.id = uuid.uuid1()
        self.name = name
        self.email = email
        self.assigned_cards = []
    
    def update_user(self, name: str, email: email):
        self.name = name if not name is None else self.name
        self.email = email if not email is None else self.email

