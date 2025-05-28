

from src.entities.schedule_tag import ScheduleTagEntity


class ScheduleTagRepositoryTag:
  def __init__(self):
    self.schedule_tags = [
      {
        "schedule_tag_id": 1
        "name": "Tag 24",
        "description": "Tag 24",
      },
      {
        "schedule_tag_id": 2 
        "name": "Tag 2",
        "description": "Tag 2",
      },
    ]
  
  def createScheduleTag(self, schedule_tag: ScheduleTagEntity):
    try:
      # Simulate creating a user
      new_schedule_tag = {
        "schedule_tag_id": schedule_tag.schedule_tag_id,
        "name": schedule_tag.name,
        "description": schedule_tag.description 
      }
      self.schedule_tags.append(new_schedule_tag)
      return True
    except Exception as e:
      raise Exception(f"Erro ao Criar Tag de agendamento: {e}")
    