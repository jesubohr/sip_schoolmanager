import unittest
from applications.schoolmanager.modules.repository.student_repository import StudentRepository
from applications.schoolmanager.modules.factory.student_factory import StudentFactory
from applications.schoolmanager.modules.models.student import Student

class StudentRepositoryTest(unittest.TestCase):
  _test_student_code: str

  def setUp(self):
    self.student_repository = StudentRepository()

  def test_create(self):
    student = {
      'first_name': 'John',
      'last_name': 'Doe',
      'birthdate': '2000-01-01',
      'email': 'johndoe@gmail.com',
      'phone': '123456789',
      'classroom_id': 1
    }
    result = self.student_repository.create(student)
    self._test_student_code = result['data']
    self.assertEqual(result['status'], 'success')

  def test_read(self):
    result = self.student_repository.read(self._test_student_code)
    self.assertIsNotNone(result)

  def test_read_all(self):
    result = self.student_repository.read_all()
    self.assertIsNotNone(result)

  def test_update(self):
    student = {
      'first_name': 'Jane',
      'last_name': 'Doe',
      'birthdate': '2000-01-01',
      'email': 'janedoe@gmail.com',
      'phone': '123456789',
      'classroom_id': 1
    }
    self.student_repository.update(student)
    result = self.student_repository.read(self._test_student_code)
    self.assertEqual(result.first_name, 'Jane')

  def test_delete(self):
    self.student_repository.delete(self._test_student_code)
    result = self.student_repository.read(self._test_student_code)
    self.assertIsNone(result)

  def test_read_by_classroom(self):
    classroom_id = 1
    result = self.student_repository.read_by_classroom(classroom_id)
    self.assertIsNotNone(result)

  def tearDown(self):
    del self.student_repository

class StudentFactoryTest(unittest.TestCase):
    def setUp(self):
      self.student_factory = StudentFactory()
  
    def test_create(self):
      student = {
        'student_code': '123456789',
        'first_name': 'John',
        'last_name': 'Doe',
        'birthdate': '2000-01-01',
        'email': 'johndoe@gmail.com',
        'phone': '123456789',
        'classroom_id': 1
      }
      result = self.student_factory.create_student(student)
      self.assertIsInstance(result, Student)

    def tearDown(self):
      del self.student_factory

class StudentTest(unittest.TestCase):
    def setUp(self):
      self.student = Student('123456789', 'John', 'Doe', '2000-01-01', 'johndoe@gmail.com', '123456789', 1)

    def test_student_code(self):
      self.assertEqual(self.student.student_code, '123456789')

    def test_email(self):
      self.assertEqual(self.student.email, 'johndoe@gmail.com')
      
    def test_classroom_id(self):
      self.assertEqual(self.student.classroom_id, 1)

    def tearDown(self):
      del self.student

if __name__ == '__main__':
  unittest.main()
