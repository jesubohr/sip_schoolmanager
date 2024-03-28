import json
from applications.schoolmanager.modules.repository.attendance_repository import AttendanceRepository
from applications.schoolmanager.modules.renderer.attendance_renderer import AttendanceRenderer

def index():
  ''' Return all attendances '''
  attendance_renderer = AttendanceRenderer()
  attendance = attendance_renderer.render_attendances_tables()
  return { 'status': 'success', 'attendance': attendance }

def update_attendance():
  ''' Update an attendance '''
  if not request.env.request_method == 'POST': raise HTTP(403)
  
  attendance_repository = AttendanceRepository()
  body = json.loads(request.body.read())
  attendance_repository.save_attendance(attendance={
    'student_id': body['studentId'],
    'subject_id': body['subjectId'],
    'attended': True if int(body['attended']) == 1 else False
  })
  return response.json({ 'status': 'success' })
