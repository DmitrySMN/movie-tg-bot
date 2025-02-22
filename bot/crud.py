from sqlalchemy.orm import Session 
from bot.models.users import Users

def create_user(session: Session, username: str) -> None:
    new_user = Users(username=username, favorites=[])
    session.add(new_user)
    session.commit()

def get_user_by_username(session: Session, username: str):
    user = session.query(Users).filter(Users.username == username).first()
    return user if user else None

def update_user_favorites(session: Session, username: str, film_id: int):
    user = get_user_by_username(session, username)
    user.favorites.append(film_id)
    session.commit()