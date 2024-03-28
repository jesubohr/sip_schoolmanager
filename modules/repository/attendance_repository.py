from gluon.dal import Field
from applications.schoolmanager.modules.repository.database_repository import DatabaseRepository

class AttendanceRepository(DatabaseRepository):
  ''' Class for attendance repository '''

  def __init__(self):
    DatabaseRepository.__init__(self)

    self.table = self.db.define_table('attendances',
      Field('student_id', 'integer', required=True),
      Field('subject_id', 'integer', required=True),
      Field('attended', 'boolean', required=True)
    )
  
  def read(self, attendance_id: int) -> dict:
    ''' Reads an attendance '''
    attendance = self.table(attendance_id)
    return { 'status': 'success', 'data': attendance }
  
  def read_all(self) -> dict:
    ''' Reads all attendances '''
    attendances = self.db(self.table.id > 0).select()
    formatted_list = []
    for attendance in attendances:
      formatted_list.append(f"{attendance.student_id}-{attendance.subject_id}-{attendance.attended}")
    return { 'status': 'success', 'data': formatted_list }
  
  def save_attendance(self, attendance: dict):
    ''' Creates or updates an attendance '''
    attendance_id = self.table.update_or_insert(
      (self.table.student_id == attendance['student_id']) & 
      (self.table.subject_id == attendance['subject_id']),
      student_id=attendance['student_id'],
      subject_id=attendance['subject_id'],
      attended=attendance['attended']
    )
    return { 'status': 'success', 'data': attendance_id }
    
