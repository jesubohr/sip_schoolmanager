from datetime import datetime

def get_student_code(data: str = '') -> str:
  ''' Generate a random student code '''
  # Return the first 9 hashed characters of the data
  # If no data is provided, use the current datetime
  data = data if data else str(datetime.now())
  return str(hash(data))[:9]
