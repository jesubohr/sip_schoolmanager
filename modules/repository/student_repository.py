from gluon.dal import Field
from applications.schoolmanager.modules.repository.database_repository import DatabaseRepository
from applications.schoolmanager.modules.models.student import Student
from applications.schoolmanager.modules.utils.student_code import get_student_code

class StudentRepository(DatabaseRepository):
  ''' Class for student repository '''

  def __init__(self):
    DatabaseRepository.__init__(self)

    self.table = self.db.define_table('students',
      Field('student_code', 'string', length=9, required=True, unique=True),
      Field('first_name', 'string', length=50, required=True),
      Field('last_name', 'string', length=50, required=True),
      Field('birthdate', 'date', required=True),
      Field('email', 'string', length=200, required=True, unique=True),
      Field('phone', 'string', length=15, required=True),
      Field('classroom_id', 'integer', required=True)
    )

  def create(self, student: Student) -> dict:
    ''' Creates a new student '''

    student_exists = self.db(self.table.email == student.email).select().first()
    if student_exists:
      return { 'status': 'error', 'error': 'Student already exists' }

    student_code = get_student_code(f"{student.first_name} {student.last_name} - {student.email}")
    self.table.insert(
      student_code=student_code,
      first_name=student.first_name,
      last_name=student.last_name,
      birthdate=student.birthdate,
      email=student.email,
      phone=student.phone,
      classroom_id=student.classroom_id
    )
    return { 'status': 'success', 'data': student_code }

  def read(self, student_code: str) -> Student:
    ''' Reads a student '''
    return self.db(self.table.student_code == student_code).select().first()

  def read_all(self) -> list:
    ''' Reads all students '''
    return self.db(self.table.id > 0).select()

  def update(self, student: Student) -> None:
    ''' Updates a student '''
    self.table(student.id).update_record(
      first_name=student.first_name,
      last_name=student.last_name,
      birthdate=student.birthdate,
      email=student.email,
      phone=student.phone,
      classroom_id=student.classroom_id
    )

  def delete(self, student_code: str) -> None:
    ''' Deletes a student '''
    self.table(student_code).delete_record()

  def read_by_classroom(self, classroom_id: int) -> list:
    ''' Reads all students by classroom '''
    return self.db(self.table.classroom_id == classroom_id).select()

  def __del__(self):
    self.db.commit()
    self.db.close()
