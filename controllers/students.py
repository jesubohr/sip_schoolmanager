import json
from applications.schoolmanager.modules.factory.student_factory import StudentFactory
from applications.schoolmanager.modules.repository.student_repository import StudentRepository

def index():
  ''' Return students view '''
  student_repository = StudentRepository()
  form_model = student_repository.table
  grid = SQLFORM.grid(
    form_model,
    user_signature=False,
    orderby='first_name',
    sortable=True,
    paginate=10,
    csv=False
  )
  return dict(grid=grid)

def add():
  ''' Show students form '''
  return dict()

def create():
  ''' Create a new student '''
  if not request.env.request_method == 'POST': raise HTTP(403)
  
  student_repository = StudentRepository()
  body = json.loads(request.body.read())

  new_student = StudentFactory.create_student(data={
    'first_name': body['firstName'],
    'last_name': body['lastName'],
    'birthdate': body['birthdate'],
    'email': body['email'],
    'phone': body['phone'],
    'classroom_id': body['classroomId'],
  })
  create_response = student_repository.create(new_student)
  return response.json(create_response)
