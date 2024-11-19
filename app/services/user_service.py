from models.user import User
from repositories.user_repository import UserRepository

class UserServices:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self, name: str, email: str, password: str):
        try:
            user = User(name=name, email=email, password=password)

            registered = self.repository.search_user_by_email(email=user.email)

            if registered:
                print("Usuário já cadastrado!")
                return
            
            self.repository.save_user(user=user)
            print("Usuário cadastrado com sucesso!")
        except TypeError as error:
            print(f"Erro ao salvar o usuário: {error}")
        except Exception as error:
            print(f"Ocorreu um erro inesperado: {error}")

    def list_all_users(self):
        return self.repository.list_users()