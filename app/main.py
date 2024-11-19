from models.user import User
from services.user_service import UserServices
from repositories.user_repository import UserRepository
from config.connection import Session
import os

def main():
    session = Session()
    repository = UserRepository(session)
    service = UserServices(repository)

    while True:

        print("=== SENAI SOLUTION === ")
        print("1 - Adicionar usuário")
        print("2 - Pesquisar um usuário")
        print("3 - Atualizar dados de um usuário")
        print("4 - Excluir um usuário")
        print("5 - Exibir todos os usuários cadastrados")
        print("0 - Sair")
        menu = int(input("Escolha uma opção: "))

        match menu:

            case 1:
                os.system("cls || clear")
                nome = str(input("Digite o seu nome: "))
                email = str(input("Digite o seu email: "))
                senha = str(input("Digite a sua senha: "))

                user = User(name=nome, email=email, password=senha)
                session.add(user)
                session.commit()
                print()
            case 2:
                os.system("cls || clear")
                email_user = str(input("Digite o email do usuário: "))
                user = session.query(User).filter_by(email=email_user).first()
                if user:
                    os.system("cls || clear")
                    print(f"{user.name} - {user.email} - {user.password}")
                else:
                    print("Usuário não encontrado!")
            case 3:
                os.system("cls || clear")
                email_user = str(input("Digite o email do usuário: "))
                user = session.query(User).filter_by(email=email_user).first()
                if user:
                    os.system("cls || clear")
                    user.name = str(input("Digite o seu nome: "))
                    user.email = str(input("Digite o seu email: "))
                    user.password = str(input("Digite a sua senha: "))
                    session.commit()
                else:
                    print("Usuário não encontrado!")
            case 4:
                os.system("cls || clear")
                email_user = str(input("Digite o email do usuário: "))
                user = session.query(User).filter_by(email=email_user).first()
                if user:
                    os.system("cls || clear")
                    session.delete(user)
                    session.commit()
                    print("Usuário deletado com sucesso!")
                else:
                    print("Usuário não encontrado!")
            case 5:
                os.system("cls || clear")
                print("\nListando usuários do banco de dados")
                os.system("cls || clear")
                list_users = session.query(User).all()
                for user in list_users:
                    print(f"{user.name} - {user.email} - {user.password}")
            case 0:
                break

if __name__ == "__main__":
    os.system("cls || clear")
    main()