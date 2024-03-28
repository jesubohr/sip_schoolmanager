import json
from applications.schoolmanager.modules.factory.classroom_factory import ClassromFactory
from applications.schoolmanager.modules.repository.classroom_repository import ClassroomRepository

def index():
  ''' Return classrooms view '''
  classroom_repository = ClassroomRepository()
  form_model = classroom_repository.table
  grid = SQLFORM.grid(
    form_model,
    user_signature=False,
    orderby='name',
    sortable=True,
    paginate=10,
    csv=False
  )
  return dict(grid=grid)

def get_all():
  ''' Return all classrooms '''
  classroom_repository = ClassroomRepository()
  classrooms = classroom_repository.read_all()
  return response.json(classrooms)

def create():
  ''' Create a new classroom '''
  if not request.env.request_method == 'POST': raise HTTP(403)
  
  classroom_repository = ClassroomRepository()
  classroom_factory = ClassromFactory()
  body = json.loads(request.body.read())

  new_classroom = classroom_factory.create_classroom(data={
    'name': body['name'],
    'description': body['description'],
    'representative': body['representative']
  })
  create_response = classroom_repository.create(new_classroom)
  return response.json(create_response)
