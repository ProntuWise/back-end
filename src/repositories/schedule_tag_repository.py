from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from scripts.db_connection import Conexao
from src.entities.schedule_tag import ScheduleTagEntity
from src.models.schedule_tag import ScheduleTagModel

class ScheduleTagRepository:        
   def create_schedule_tag(self, schedule_tag: ScheduleTagEntity):
        try:
           print("Iniciando criação de schedule tag...")
           
           new_schedule_tag = ScheduleTagModel(
               name=schedule_tag.name,
               description=schedule_tag.description
           )
           
           with Conexao().session as session:
           
            print("Adicionando nova tag...")
            session.add(new_schedule_tag)
            print("Commitando alterações...")
            session.commit()
            print("Schedule tag criada com sucesso!")
           
            # Obtendo o ID antes de fechar a sessão
            schedule_tag.schedule_tag_id = new_schedule_tag.schedule_tag_id
            
            return schedule_tag
           
        except IntegrityError as e:
            print(f"Erro de integridade: {str(e)}")
            raise Exception("Schedule Tag com esse nome já existe.")
        except SQLAlchemyError as e:
            print(f"Erro do SQLAlchemy: {str(e)}")
            raise Exception(f"Erro interno de banco de dados: {str(e)}")
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            raise Exception(f"Erro interno: {str(e)}")
        finally:
            if session:
                print("Fechando sessão...")
                session.close()