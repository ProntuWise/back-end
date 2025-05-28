from src.entities.patient import PatientEntity

class PatientRepositoryMock:
    def __init__(self):
        self.patients = []
        self.next_id = 1

    def create_patient(self, patient: PatientEntity) -> PatientEntity:
        try:
            # Simula a criação de um novo paciente
            patient.patient_id = self.next_id
            self.next_id += 1
            
            # Adiciona à lista de pacientes
            self.patients.append(patient)
            
            return patient
            
        except Exception as e:
            print(f"Erro no mock ao criar paciente: {str(e)}")
            raise Exception(f"Erro interno do mock: {str(e)}")
