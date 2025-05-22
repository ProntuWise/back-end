import enum

class AppointmentStatusEnum(enum.Enum):
    Scheduled = 'Scheduled'
    Confirmed = 'Confirmed'
    Cancelled = 'Cancelled'
    Completed = 'Completed'