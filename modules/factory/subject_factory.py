from applications.schoolmanager.modules.singleton import Singleton
from applications.schoolmanager.modules.models.subject import Subject

class SubjectFactory(metaclass = Singleton):
  def __init__(self):
    self._cache = {}

  def create_subject(self, data: dict) -> Subject:
    ''' Create new Subject instance or returns existing one '''

    key = hash(frozenset(data.items()))
    if key not in self._cache:
      self._cache[key] = Subject(
        name = data['name'],
        description = data['description']
      )
    return self._cache[key]
