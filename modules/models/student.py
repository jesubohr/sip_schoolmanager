from datetime import date

class Student:
  def __init__(self, student_code: str, first_name: str, last_name: str, birthdate: date, email: str, phone: str, classroom_id: int):
    self.student_code = student_code
    self.first_name = first_name
    self.last_name = last_name
    self.birthdate = birthdate
    self.email = email
    self.phone = phone
    self.classroom_id = classroom_id

  def __str__(self):
    return f'{self.student_code} - {self.first_name} {self.last_name}'
