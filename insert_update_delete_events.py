from pickle import FALSE
from pprint import pprint
from Google import Create_Service,convert_to_RFC_datetime

CLIENT_SECRET_FILE = 'secret_file.json'
API_NAME = 'calendar'
VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,VERSION,SCOPES)

code_clinic_id = 'c_sua93ie12ttvjafrd647og4dl8@group.calendar.google.com'
year = 2020
month = 11
day = 25
shour = 13
ehour = 15
minutes = 30
"""
create an event
"""
my_colours = service.colors().get().execute()
# pprint(my_colours)

recurrence = [
    'RRULE:FREQ=MONTHLY;COUNT=2'
]
##########################################################################################
###  ADD EVENT ADD EVENT ADD EVENT ADD EVENT ADD EVENT ADD EVENT  ADD EVENT  ADD EVENT ###
##########################################################################################
hour_adjustment = +2
event_request_body = {
    "start" : {
        'dateTime' : convert_to_RFC_datetime(year,month,day,shour,minutes),
        'timeZone' :  "Africa/Johannesburg"
    },
    'end' : {
        'dateTime' : convert_to_RFC_datetime(year,month,day,ehour,minutes),
        'timeZone' :  "Africa/Johannesburg"
    },
    'summary' : "code clinic",
    'description': "assist with recurrsion",
    'colorId' :  5,
    'status' : "confirmed",
    'transprency' : 'opaque',
    'visibility' : "public",
    'location' : 'wethinkcode',
    'attendees' : [
        {
            'displayName' : 'Jeff',
            'comment' : 'I Need help',
            'email' : 'mjohanni@student.wethinkcode.co.za',
            'optional' : False,
            'organizer' : True,
            'responseStatus': 'accepted'
        },
    ],
    'recurrence' : recurrence
#     "creator": {
#     "id": string,
#     "email": string,
#     "displayName": string,
#     "self": boolean
#   },
#   "organizer": {
#     "id": string,
#     "email": string,
#     "displayName": string,
#     "self": boolean
#   }
}

maxAttendees = 3
sendNotifications = True
sendUpdates = 'none'
supportsAttachments = False

response = service.events().insert(
    calendarId = code_clinic_id,
    maxAttendees=maxAttendees,
    sendNotifications=sendNotifications,
    sendUpdates=sendUpdates,
    supportsAttachments=supportsAttachments,
    body=event_request_body
).execute()

pprint(response)

eventId = response['id']

##########################################################################################
###    UPDATE EVENT    UPDATE EVENT    UPDATE EVENT    UPDATE EVENT    UPDATE EVENT    ###
##########################################################################################

start_datetime = convert_to_RFC_datetime(2020,11,26,13,30)
end_datetime = convert_to_RFC_datetime(2020,11,26,15,30)
response ['start']['dateTime'] = start_datetime
response['end']['dateTime'] = end_datetime
response['summary'] = 'changed Time'
response['Description'] = 'instead of recursion lets do toy Robot 5'
service.events().update(
    calendarId = code_clinic_id,
    eventId = eventId,
    body = response).execute()


##########################################################################################
###    DELETE EVENT    DELETE EVENT    DELETE EVENT    DELETE EVENT    DELETE EVENT    ###
##########################################################################################


service.events().delete(
    calendarId=code_clinic_id,
    eventId=eventId).execute()