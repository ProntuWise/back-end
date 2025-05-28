from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from scripts.db_connection import Conexao
from src.entities.patient import PatientEntity
from src.models.patient import Patient

class PatientRepository:        
    def create_patient(self, patient: PatientEntity):
        try:
            print("Iniciando criação de paciente...")
            
            new_patient = Patient(
                name=patient.name,
                cpf=patient.cpf,
                rg=patient.rg,
                birth_date=patient.birth_date,
                phone=patient.phone,
                email=patient.email,
                address=patient.address,
                gender=patient.gender,
                folder_path=patient.folder_path
            )
            
            with Conexao().session as session:
                print("Adicionando novo paciente...")
                session.add(new_patient)
                print("Commitando alterações...")
                session.commit()
                print("Paciente criado com sucesso!")
                
                # Obtendo o ID antes de fechar a sessão
                patient.patient_id = new_patient.patient_id
                
                return patient
                
        except IntegrityError as e:
            print(f"Erro de integridade: {str(e)}")
            raise Exception("CPF já cadastrado no sistema.")
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
