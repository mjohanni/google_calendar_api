from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'secret_file.json'
API_NAME = 'calendar'
VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,VERSION,SCOPES)
