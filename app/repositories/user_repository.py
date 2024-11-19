from models.user import User
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = Session

    def save_user(self, user: User):
        self.session.add(user)
        self.session.commit()

    def search_user_by_email(self, email:str):
        return self.session.query(User).filter_by(email = email).first()
    
    def delete_user(self, user: User):
        self.session.delete(user)
        self.session.commit()

    def list_users(self):
        return self.session.query(User).all()