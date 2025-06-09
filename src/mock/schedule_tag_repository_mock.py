from src.entities.schedule_tag import ScheduleTagEntity


class ScheduleTagRepositoryMock:
  def __init__(self):
    self.schedule_tags = [
      {
        "schedule_tag_id": 1,
        "name": "Tag 24",
        "description": "Tag 24",
      },
      {
        "schedule_tag_id": 2 ,
        "name": "Tag 2",
        "description": "Tag 2",
      },
    ]
    self.next_id = 3
  
  def create_schedule_tag(self, schedule_tag: ScheduleTagEntity) -> ScheduleTagEntity:
    try:
      # Simulate creating a tag
      schedule_tag.schedule_tag_id = self.next_id
      self.next_id += 1
      
      new_schedule_tag = {
        "schedule_tag_id": schedule_tag.schedule_tag_id,
        "name": schedule_tag.name,
        "description": schedule_tag.description 
      }
      self.schedule_tags.append(new_schedule_tag)
      return schedule_tag
    except Exception as e:
      raise Exception(f"Erro ao Criar Tag de agendamento: {e}")
    