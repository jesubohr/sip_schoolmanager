from gluon.contrib.appconfig import Appconfig
from gluon import DAL

class DatabaseRepository():
  ''' Class for database connection '''
  config = Appconfig(reload=True)
  
  def __init__(self):
    database_uri = self.create_database_uri()
    self.db = DAL(database_uri, pool_size=self.config.get('db.pool_size', cast=int), migrate=self.config.get('db.migrate', cast=bool), check_reserved=['all'])

  def get_database_uri(self) -> str:
    ''' Creates uri connection string '''

    user = self.config.get('postgres.user')
    password = self.config.get('postgres.password')
    host = self.config.get('postgres.host')
    database = self.config.get('postgres.database')
    
    uri: str = self.config.get('db.uri')
    return uri.format(user=user, password=password, host=host, database=database)
