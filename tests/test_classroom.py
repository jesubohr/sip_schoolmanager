import unittest
from applications.schoolmanager.modules.repository.classroom_repository import ClassroomRepository
from applications.schoolmanager.modules.factory.classroom_factory import ClassroomFactory
from applications.schoolmanager.modules.models.classroom import Classroom

class ClassroomRepositoryTest(unittest.TestCase):
  _test_classroom_id: str

  def setUp(self):
    self.classroom_repository = ClassroomRepository()

  def test_create(self):
    classroom = {
      'name': 'Class A',
      'description': 'Class A description',
      'representative': 1
    }
    result = self.classroom_repository.create(classroom)
    self._test_classroom_id = result['data']
    self.assertEqual(result['status'], 'success')

  def test_read(self):
    result = self.classroom_repository.read(self._test_classroom_id)
    self.assertIsNotNone(result)

  def test_read_all(self):
    result = self.classroom_repository.read_all()
    self.assertIsNotNone(result)

  def test_update(self):
    classroom = {
      'name': 'Class B',
      'description': 'Class B description',
      'representative': 1
    }
    self.classroom_repository.update(classroom)
    result = self.classroom_repository.read(self._test_classroom_id)
    self.assertEqual(result.name, 'Class B')

  def test_delete(self):
    self.classroom_repository.delete(self._test_classroom_id)
    result = self.classroom_repository.read(self._test_classroom_id)
    self.assertIsNone(result)

  def tearDown(self):
    del self.classroom_repository

class ClassroomFactoryTest(unittest.TestCase):
    def setUp(self):
      self.classroom_factory = ClassroomFactory()

    def test_create(self):
      classroom = {
        'name': 'Class A',
        'description': 'Class A description',
        'representative': 1
      }
      result = self.classroom_factory.create_classroom(classroom)
      self.assertIsInstance(result, Classroom)

    def tearDown(self):
      del self.classroom_factory

if __name__ == '__main__':
  unittest.main()
