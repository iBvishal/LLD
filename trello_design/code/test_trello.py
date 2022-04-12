import email
from pydoc import describe
from unicodedata import name
from board import Board
from enums import BoardStatus
from user import User

def _create_user(name: str, email: email):
    user = User(
        name = name,
        email = email
    )
    return user

def test_create_user():
    user = _create_user("Vishal", "vishalb@esper.io")
    assert user != None
    assert user.name == "Vishal"
    assert user.email == "vishalb@esper.io"

def test_create_board():
    user = _create_user(name = "Vishal", email = "vishalb@esper.io")
    board = Board(
        created_by = user, 
        name = "Team1", 
        description = "abc"
        )
    assert board != None
    assert board.created_by.id == user.id
    assert board.status == BoardStatus.PUBLIC.value
    assert board.url == "board/" + str(board.id) + "/"

def test_create_column_in_board():
    user = _create_user(name = "Vishal", email = "vishalb@esper.io")
    board = Board(
        created_by = user, 
        name = "Team1", 
        description = "abc"
        )
    board.create_column("A")
    board.create_column("B")


    assert len(board.columns) == 2
    column1 = board.columns[0]
    column2 = board.columns[1]
    assert column1.url == "column/" + str(column1.id) + "/"
    assert column2.url == "column/" + str(column2.id) + "/"

def test_create_card_in_column():
    user = _create_user(name = "Vishal", email = "vishalb@esper.io")
    board = Board(
        created_by = user, 
        name = "Team1", 
        description = "abc"
        )
    board.create_column("A")
    column = board.columns[0]
    # assert column.cards is None
    column.create_card(
        name = "1134: ACBCBC",
        description = "this is the description",
        user = user
    )
    card = column.cards[0]
    assert len(column.cards) == 1
    assert card.url == "card/" + str(card.id) + "/"