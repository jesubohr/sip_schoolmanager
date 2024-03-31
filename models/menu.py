# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
# this is the main application menu add/remove items as required

response.menu = []
if not configuration.get('app.production'):
  _app = request.application
  response.menu += [
    (T('Estudiantes'), False, '#', [
      (T('Ver Estudiantes'), False, URL('students', 'index')),
      (T('Agregar Estudiante'), False, URL('students', 'add')),
    ]),
    (T('Salones'), False, URL('classrooms', 'index')),
    (T('Materias'), False, URL('subjects', 'index')),
    (T('Asistencias'), False, URL('attendances', 'index')),
  ]
