from gluon.dal import Field
from applications.schoolmanager.modules.repository.database_repository import DatabaseRepository
from applications.schoolmanager.modules.models.subject import Subject

class SubjectRepository(DatabaseRepository):
  ''' Class for subject repository '''
  
  def __init__(self):
    DatabaseRepository.__init__(self)

    self.table = self.db.define_table('subjects',
      Field('name', 'string', length=100, required=True, unique=True),
      Field('description', 'string', length=200)
    )

  def create(self, subject: Subject) -> dict:
    ''' Creates a new subject '''
    subject_id = self.table.insert(name=subject.name, description=subject.description)
    return { 'status': 'success', 'data': subject_id }

  def read(self, id: int) -> Subject:
    ''' Reads a subject '''
    return self.table(id)

  def read_all(self) -> list:
    ''' Reads all subjects '''
    return self.db(self.table.id > 0).select()

  def update(self, subject: Subject) -> None:
    ''' Updates a subject '''
    self.table(subject.id).update_record(name=subject.name, description=subject.description)

  def delete(self, id: int) -> None:
    ''' Deletes a subject '''
    self.table(id).delete_record()

  def __del__(self):
    self.db.commit()
    self.db.close()
