routers = dict(
  BASE = dict(
    default_application='schoolmanager',
  ),
  schoolmanager = dict(
    default_controller='default',
    default_function='index',
    functions = dict(
      default=['index'],
      students=['index', 'add', 'create'],
      subjects=['index'],
      classrooms=['index', 'get_all', 'create'],
      attendances=['index', 'update_attendance']    
    )
  ),
)
