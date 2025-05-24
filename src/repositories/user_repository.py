from sqlalchemy import insert
from src.models.user import User
from src.entities.user import User as UserEntity
from scripts.db_connection import Conexao

class UserRepository:
  def createUser(self, user: UserEntity):
    try:
      # Commmand to insert user into the database
      new_user = insert(User).values(
        username=user.name,
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
    except Exception as e:
      raise Exception(f"Erro ao Criar Usuário: {e}")