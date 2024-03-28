from typing import List
from gluon.html import *
from pydal.objects import Row
from applications.schoolmanager.modules.repository.attendance_repository import AttendanceRepository
from applications.schoolmanager.modules.repository.classroom_repository import ClassroomRepository
from applications.schoolmanager.modules.repository.student_repository import StudentRepository
from applications.schoolmanager.modules.repository.subject_repository import SubjectRepository

class AttendanceRenderer:
  def __init__(self):
    self.classroom_repository = ClassroomRepository()
    self.student_repository = StudentRepository()
    self.subject_repository = SubjectRepository()
    self.attendance_repository = AttendanceRepository()

  def render_attendances_tables(self) -> DIV:
    classrooms = self.classroom_repository.read_all()
    classrooms_elements = []
    for classroom in classrooms:
      classroom_element = self.render_classroom_attendance(classroom)
      classrooms_elements.append(classroom_element)
    return DIV(*classrooms_elements, _class='classrooms-container')

  def render_classroom_attendance(self, classroom: Row) -> DIV:
    students = self.student_repository.read_by_classroom(classroom.id)
    subjects = self.subject_repository.read_all()

    if not students:
      return DIV(H2(f"Salón {classroom.name}"), P('No hay estudiantes registrados'), _class='classroom-container')

    table_header = self.render_table_header(subjects)
    table_body = self.render_table_body(students)

    table = TABLE(table_header, table_body, _class='attendance-table')
    return DIV(H2(f"Salón {classroom.name}"), table, _class='classroom-container')

  def render_table_header(self, subjects: List[Row]) -> THEAD:
    subjects_elements = []
    for subject in subjects:
      subject_element = TH(subject.name, _scope='col')
      subjects_elements.append(subject_element)
    return THEAD(
      TR(
        TH('Nombre', _scope='col'),
        *subjects_elements
      )
    )

  def render_table_body(self, students: List[Row]) -> TBODY:
    students_elements = self.render_students(students)
    return TBODY(*students_elements)

  def render_students(self, students: List[Row]) -> List[TR]:
    students_elements = []
    for student in students:
      student_element = self.render_student(student)
      students_elements.append(student_element)
    return students_elements

  def render_student(self, student: Row) -> DIV:
    subjects = self.subject_repository.read_all()
    subjects_elements = self.render_subjects(subjects, student.id)
    full_name = f'{student.first_name} {student.last_name}'
    return TR(
      TH(full_name),
      *subjects_elements
    )

  def render_subjects(self, subjects: List[Row], student_id: int) -> List[DIV]:
    subjects_elements = []
    for subject in subjects:
      subject_element = TD(self.render_subject(student_id, subject.id))
      subjects_elements.append(subject_element)
    return subjects_elements

  def render_subject(self, student_id: int, subject_id: int) -> SELECT:
    attendances_list = self.attendance_repository.read_all()['data']
    attendance_value = self.get_attendance_value(attendances_list, student_id, subject_id)
    return SELECT(
      OPTION('-- Opción --', _value='2', _selected='selected', _disabled='disabled'),
      OPTION('Asistió', _value='1'),
      OPTION('Ausente', _value='0'),
      _value='2',
      value=attendance_value,
      _class='attendance-select',
      _name=f'attendance_{student_id}_{subject_id}'
    )

  def get_attendance_value(self, attendances_list: List[Row], student_id: int, subject_id: int) -> int:
    attended = f"{student_id}-{subject_id}-True"
    not_attended = f"{student_id}-{subject_id}-False"
    return 1 if attended in attendances_list else 0 if not_attended in attendances_list else 2
