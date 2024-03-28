import json
from applications.schoolmanager.modules.repository.subject_repository import SubjectRepository

def index():
  ''' Return subject view '''
  subject_repository = SubjectRepository()
  form_model = subject_repository.table
  grid = SQLFORM.grid(
    form_model,
    user_signature=False,
    orderby='name',
    sortable=True,
    paginate=10,
    csv=False
  )
  return dict(grid=grid)
