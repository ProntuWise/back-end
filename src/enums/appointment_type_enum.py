import enum

class AppointmentTypeEnum(enum.Enum):
    First_Visit = 'First_Visit'
    Recent_Followup = 'Recent_Followup'
    Late_Followup = 'Late_Followup'