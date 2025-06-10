from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from scripts.db_connection import Conexao
from src.entities.appointment import AppointmentEntity
from src.models.appointment import AppointmentModel
from src.schemas.appointment_schema import AppointmentCreateRequest, AppointmentUpdateRequest
from fastapi import HTTPException

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
    
    def get_appointments(self):
        try:
            appointments_list = []
            query = select(AppointmentModel)
            print("Query SQL gerada:", str(query))

            with Conexao().session as session:
                print("Executando query...")
                result = session.execute(query)
                print("Query executada, obtendo resultados...")
                appointments = result.scalars().all()
                print("Número de appointments encontrados:", len(appointments))
                
                # Convertendo os modelos para dicionários
                for appointment in appointments:
                    appointment_dict = {
                        'appointment_id': appointment.appointment_id,
                        'date': str(appointment.date),
                        'time': str(appointment.time),
                        'duration': appointment.duration,
                        'patient_id': appointment.patient_id,
                        'user_id': appointment.user_id,
                        'tag_id': appointment.tag_id,
                        'description': appointment.description,
                        'status': appointment.status.value if appointment.status else None,
                        'appointment_type': appointment.appointment_type.value if appointment.appointment_type else None,
                        'created_at': str(appointment.created_at) if appointment.created_at else None
                    }
                    print(f"Processando appointment {appointment.appointment_id}:", appointment_dict)
                    appointments_list.append(appointment_dict)
                
                print("Total de appointments processados:", len(appointments_list))
                return appointments_list
        except SQLAlchemyError as e:
            print(f"Erro do SQLAlchemy ao buscar appointments: {str(e)}")
            raise Exception(f"Erro ao consultar banco de dados: {str(e)}")
        except Exception as e:
            print(f"Erro inesperado ao buscar appointments: {str(e)}")
            raise Exception(f"Erro interno: {str(e)}")
        finally:
            if session:
                print("Fechando sessão...")
                session.close()
    
    def update_appointment(self, appointment_id: int, request: AppointmentUpdateRequest):
        try:
            with Conexao().session as session:
                appointment = session.query(AppointmentModel).filter(AppointmentModel.appointment_id == appointment_id).first()
                if not appointment:
                    raise HTTPException(status_code=404, detail="Agendamento não encontrado")
                
                # Atualiza apenas os campos que foram fornecidos
                if request.date is not None:
                    appointment.date = request.date
                if request.time is not None:
                    appointment.time = request.time
                if request.duration is not None:
                    appointment.duration = request.duration
                if request.patient_id is not None:
                    appointment.patient_id = request.patient_id
                if request.user_id is not None:
                    appointment.user_id = request.user_id
                if request.tag_id is not None:
                    appointment.tag_id = request.tag_id
                if request.description is not None:
                    appointment.description = request.description
                if request.status is not None:
                    appointment.status = request.status
                if request.appointment_type is not None:
                    appointment.appointment_type = request.appointment_type
                
                session.commit()
                return appointment
        except SQLAlchemyError as e:
            print(f"Erro do SQLAlchemy ao atualizar appointment: {str(e)}")
            raise Exception(f"Erro ao atualizar banco de dados: {str(e)}")
        except Exception as e:
            print(f"Erro inesperado ao atualizar appointment: {str(e)}")
            raise Exception(f"Erro interno: {str(e)}")
        finally:
            if session:
                print("Fechando sessão...")
                session.close()
    