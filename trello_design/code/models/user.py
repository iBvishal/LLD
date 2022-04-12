import email
import uuid
from enums import UserRole

class UserModel():

    def __init__(self, name: str, email: email, role: UserRole = UserRole.ADMIN.value) -> None:
        self.id = uuid.uuid1()
        self.name = name
        self.email = email
        self.assigned_cards = []
        self.role = role
        self.is_active = True

