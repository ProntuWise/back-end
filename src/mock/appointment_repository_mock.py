from datetime import date, time
from src.entities.appointment import AppointmentEntity
from src.enums.appointment_status_enum import AppointmentStatusEnum
from src.enums.appointment_type_enum import AppointmentTypeEnum
from src.schemas.appointment_schema import AppointmentUpdateRequest

class AppointmentRepositoryMock:
    def __init__(self):
        self.appointments = []
        self.next_id = 1

    def create_appointment(self, appointment: AppointmentEntity) -> AppointmentEntity:
        try:
            # Simula a criação de um novo agendamento
            appointment.appointment_id = self.next_id
            self.next_id += 1
            
            # Adiciona à lista de agendamentos
            self.appointments.append(appointment)
            
            return appointment
            
        except Exception as e:
            print(f"Erro no mock ao criar agendamento: {str(e)}")
            raise Exception(f"Erro interno do mock: {str(e)}") 
    
    def get_appointments(self):
        return self.appointments

    def update_appointment(self, appointment_id: int, appointment_data: AppointmentUpdateRequest) -> AppointmentEntity:
        try:
            # Procura o agendamento pelo ID
            for i, appointment in enumerate(self.appointments):
                if appointment.appointment_id == appointment_id:
                    # Atualiza apenas os campos que foram fornecidos
                    if appointment_data.date is not None:
                        appointment.date = date.fromisoformat(appointment_data.date)
                    if appointment_data.time is not None:
                        appointment.time = time.fromisoformat(appointment_data.time)
                    if appointment_data.duration is not None:
                        appointment.duration = appointment_data.duration
                    if appointment_data.patient_id is not None:
                        appointment.patient_id = appointment_data.patient_id
                    if appointment_data.user_id is not None:
                        appointment.user_id = appointment_data.user_id
                    if appointment_data.tag_id is not None:
                        appointment.tag_id = appointment_data.tag_id
                    if appointment_data.description is not None:
                        appointment.description = appointment_data.description
                    if appointment_data.status is not None:
                        appointment.status = appointment_data.status
                    if appointment_data.appointment_type is not None:
                        appointment.appointment_type = appointment_data.appointment_type
                    
                    return appointment
            raise Exception("Agendamento não encontrado")
        except Exception as e:
            print(f"Erro no mock ao atualizar agendamento: {str(e)}")
            raise Exception(f"Erro interno do mock: {str(e)}")

    def delete_appointment(self, appointment_id: int) -> AppointmentEntity:
        try:
            # Procura o agendamento pelo ID
            for i, appointment in enumerate(self.appointments):
                if appointment.appointment_id == appointment_id:
                    # Remove e retorna o agendamento
                    return self.appointments.pop(i)
            raise Exception("Agendamento não encontrado")
        except Exception as e:
            print(f"Erro no mock ao deletar agendamento: {str(e)}")
            raise Exception(f"Erro interno do mock: {str(e)}")