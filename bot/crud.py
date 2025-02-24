from sqlalchemy import update
from sqlalchemy.orm import Session 
from bot.models.users import Users
from sqlalchemy.orm.attributes import flag_modified

def create_user(session: Session, username: str) -> None:
    new_user = Users(username=username, favorites=[])
    session.add(new_user)
    session.commit()

def get_user_by_username(session: Session, username: str) -> Users:
    user = session.query(Users).filter(Users.username == username).first()
    return user if user else None

def get_user_favorites(session: Session, username: str):
    user = session.query(Users).filter(Users.username == username).first()
    return user.favorites

def update_user_favorites(session: Session, username: str, film_id: int) -> None:
    user = session.query(Users).filter(Users.username == username).first()
    user.favorites.append(film_id)
    flag_modified(user, "favorites")
    session.commit()
    
    