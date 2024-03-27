from applications.schoolmanager.modules.models.student import Student

class StudentFactory:
  ''' Class for student factory '''

  @staticmethod
  def create_student(data: dict) -> Student:
    ''' Create new Student instance '''
    return Student(
      first_name = data['first_name'],
      last_name = data['last_name'],
      birthdate = data['birthdate'],
      email = data['email'],
      phone = data['phone'],
      classroom_id = data['classroom_id']
    )
