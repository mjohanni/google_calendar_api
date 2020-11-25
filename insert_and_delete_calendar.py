from pprint import pprint

from google.auth.transport import Response
from Google import Create_Service

CLIENT_SECRET_FILE = 'secret_file.json'
API_NAME = 'calendar'
VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,VERSION,SCOPES)

request_body = {
    'summary' : 'Code Clinic'
}
#create a calendar

response = service.calendars().insert(body = request_body).execute()
print(response)

#delete calendar
# service.calendars().delete(calendarId= 'c_62l2iodk265cd6l2umd208en40@group.calendar.google.com').execute()
