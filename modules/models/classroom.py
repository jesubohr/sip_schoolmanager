class Classroom:
  def __init__(self, name: str, description: str, representative: int):
    self.name = name
    self.description = description
    self.representative = representative
  
  def __str__(self):
    return f'{self.name} - {self.description}'
