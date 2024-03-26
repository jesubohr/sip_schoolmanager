from applications.schoolmanager.modules.singleton import Singleton
from applications.schoolmanager.modules.models.classroom import Classroom

class ClassromFactory(metaclass = Singleton):
  def __init__(self):
    self._cache = {}

  def create_classroom(self, data: dict) -> Classroom:
    ''' Create new Classroom instance or returns existing one '''

    classroom_id = data['id']
    if classroom_id not in self._cache:
      classroom = Classroom(
        name = data['name'],
        description = data['description'],
        representative = data['representative']
      )
      self._cache[classroom_id] = classroom
    return self._cache[classroom_id]
