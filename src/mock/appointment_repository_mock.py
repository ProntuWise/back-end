from datetime import date, time
from src.entities.appointment import AppointmentEntity
from src.enums.appointment_status_enum import AppointmentStatusEnum
from src.enums.appointment_type_enum import AppointmentTypeEnum

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