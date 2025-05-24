from sqlalchemy import insert
from src.models.user import User
from src.entities.user import User as UserEntity
from scripts.db_connection import Conexao
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

class UserRepository:
  def createUser(self, user: UserEntity):
    try:
      # Commmand to insert user into the database
      new_user = insert(User).values(
        username=user.username,
        password=user.password,
        name=user.name,
        role=user.role.value,
        email=user.email
      )

      # Execute the command
      with Conexao().session as session:
        session.execute(new_user)
        session.commit()

      return True
    except IntegrityError as e:
        raise Exception("Usuário com esse e-mail ou nome já existe.")
    except SQLAlchemyError as e:
        raise Exception("Erro interno ao acessar o banco de dados.")
    except Exception as e:
        raise Exception("Erro inesperado ao criar usuário.")