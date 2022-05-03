from __future__ import print_function

import base64
import os.path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# A function that sends the email of the result to hadas.c@velismedia.com.

SCOPES = 'https'


def sendemail(message):
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('gmail', 'v1', credentials=creds)
    mime_message = MIMEMultipart()
    mime_message['to'] = 'roiyad95@gmail.com'
    mime_message['subject'] = 'FinishedJob'
    mime_message.attach(MIMEText(message, 'plain'))
    raw_string = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()
    update_message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(update_message)




