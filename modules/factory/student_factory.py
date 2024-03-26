from modules.models.student import Student

class StudentFactory:
  def create_student(data: dict) -> Student:
    ''' Create new Student instance '''

    return Student(
      student_code = data['student_code'],
      first_name = data['first_name'],
      last_name = data['last_name'],
      birthdate = data['birthdate'],
      email = data['email'],
      phone = data['phone'],
      classroom_id = data['classroom_id']
    )
