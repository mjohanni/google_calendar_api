from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'secret_file.json'
API_NAME = 'calendar'
VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,VERSION,SCOPES)

response = service.calendarList().list(
    maxResults = 250,
    showDeleted = False,
    showHidden = False,
).execute()

calendar_items = response.get('items')
next_page_token = response.get('nextPageToken')

while next_page_token:
    response = service.calendarList().list(
        maxResults = 250,
        showDeleted = False,
        showHidden = False,
        page_token = next_page_token
    ).execute()
    calendar_items = response.get('items')
    next_page_token = response.get('nextPageToken')

pprint(calendar_items)

my_calendar = filter(lambda x: 'Code Clinic' in x['summary'], calendar_items)
my_calendar = next(my_calendar)

my_calendar['summary'] = 'Code Clinic'
my_calendar['description'] = 'assist with code'
my_calendar['location'] = 'WeThinkCode_'

service.calendars().update(calendarId=my_calendar['id'], body = my_calendar).execute()

# {
#   "kind": "calendar#calendar",
#   "etag": etag,
#   "id": string,
#   "summary": string,
#   "description": string,
#   "location": string,
#   "timeZone": string,
#   "conferenceProperties": {
#     "allowedConferenceSolutionTypes": [
#       string
#     ]
#   }
# }