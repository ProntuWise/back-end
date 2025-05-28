from typing import Optional

class ScheduleTagEntity:
    schedule_tag_id: Optional[int] = None
    name: str
    description: str
    
    def __init__(self, name: str, description: str, schedule_tag_id: Optional[int] = None):
        self.name = name
        self.description = description
        self.schedule_tag_id = schedule_tag_id
        
    def to_dict(self): 
        return {
            'schedule_tag_id': self.schedule_tag_id,
            'name': self.name,
            'description': self.description
        }
    
    