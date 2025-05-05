import enum

class AppointmentStatusEnum(enum.Enum):
    Scheduled = 'Scheduled'
    Confirmed = 'Confirmed'
    Canceled = 'Canceled'
    Completed = 'Completed'