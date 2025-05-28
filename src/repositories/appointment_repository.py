from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from scripts.db_connection import Conexao
from src.entities.appointment import AppointmentEntity
from src.models.appointment import AppointmentModel

class AppointmentRepository:        
    def create_appointment(self, appointment: AppointmentEntity):
        try:
            print("Iniciando criação de appointment...")
            
            new_appointment = AppointmentModel(
                date=appointment.date,
                time=appointment.time,
                duration=appointment.duration,
                patient_id=appointment.patient_id,
                user_id=appointment.user_id,
                tag_id=appointment.tag_id,
                description=appointment.description,
                status=appointment.status,
                appointment_type=appointment.appointment_type
            )
            
            with Conexao().session as session:
                print("Adicionando novo appointment...")
                session.add(new_appointment)
                print("Commitando alterações...")
                session.commit()
                print("Appointment criado com sucesso!")
                
                # Obtendo o ID antes de fechar a sessão
                appointment.appointment_id = new_appointment.appointment_id
                
                return appointment
                
        except IntegrityError as e:
            print(f"Erro de integridade: {str(e)}")
            raise Exception("Erro ao criar appointment: violação de integridade.")
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