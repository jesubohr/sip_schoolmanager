from gluon.dal import Field
from applications.schoolmanager.modules.repository.database_repository import DatabaseRepository
from applications.schoolmanager.modules.models.classroom import Classroom

class ClassroomRepository(DatabaseRepository):
  ''' Class for classroom repository '''
  
  def __init__(self):
    DatabaseRepository.__init__(self)

    self.table = self.db.define_table('classrooms',
      Field('name', 'string', length=50, required=True, unique=True),
      Field('description', 'string', length=100),
      Field('representative', 'integer', required=True)
    )

  def create(self, classroom: Classroom) -> dict:
    ''' Creates a new classroom '''
    classroom_id = self.table.insert(name=classroom.name, description=classroom.description, representative=classroom.representative)
    return { 'status': 'success', 'data': classroom_id }

  def read(self, id: int) -> Classroom:
    ''' Reads a classroom '''
    return self.table(id)

  def read_all(self) -> list:
    ''' Reads all classrooms '''
    return self.db(self.table.id > 0).select()

  def update(self, classroom: Classroom) -> None:
    ''' Updates a classroom '''
    self.table(classroom.id).update_record(name=classroom.name, description=classroom.description, representative=classroom.representative)

  def delete(self, id: int) -> None:
    ''' Deletes a classroom '''
    self.table(id).delete_record()

  def __del__(self):
    self.db.commit()
    self.db.close()
