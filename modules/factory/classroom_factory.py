from applications.schoolmanager.modules.singleton import Singleton
from applications.schoolmanager.modules.models.classroom import Classroom

class ClassromFactory(metaclass = Singleton):
  def __init__(self):
    self._cache = {}

  def create_classroom(self, data: dict) -> Classroom:
    ''' Create new Classroom instance or returns existing one '''

    key = hash(frozenset(data.items()))
    if key not in self._cache:
      self._cache[key] = Classroom(
        name = data['name'],
        description = data['description'],
        representative = data['representative']
      )
    return self._cache[key]
