import datetime
import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

CLIENT_SECRET_FILE = 'secret_file.json'
API_NAME = 'calendar'
VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = None
request_body = None

def create_service():
    global service

    new_credentials = None
    username = input("Please enter student username: ")
    email = input("please enter student email: ")
    test1 = email.split("@")
    if username in test1:
        print("working")
        test2 = email.replace(username,'')
        if "@student" in test2.split('.') and "wethinkcode" in test2.split('.'):
            print("welcome to code_clinic fellow student")
        elif "wethinkcode" in test2.split('.'):
            print("welcome admin user")
    else:
        print("please enter valid username or email")

if __name__ == '__main__':
    create_service()