class Subject:
  def __init__(self, name: str, description: str):
    self.name = name
    self.description = description

  def __str__(self):
    return f'{self.name} - {self.description}'
