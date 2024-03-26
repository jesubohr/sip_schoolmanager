from modules.singleton import Singleton
from modules.models.subject import Subject

class SubjectFactory(metaclass = Singleton):
  def __init__(self):
    self._cache = {}

  def create_subject(self, data: dict) -> Subject:
    ''' Create new Subject instance or returns existing one '''

    subject_id = data['id']
    if subject_id not in self._cache:
      subject = Subject(
        name = data['name'],
        description = data['description']
      )
      self._cache[subject_id] = subject
    return self._cache[subject_id]
