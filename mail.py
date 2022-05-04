from __future__ import print_function

import base64
import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# A function that sends the email of the result to hadas.c@velismedia.com.

SCOPES = 'https://www.googleapis.com/auth/gmail.send'

# If there is an error when running the gui , run the quick_start file to get a new token.json file
# If you don't have a credentials.json file create it using the https://console.cloud.google.com/ webstie

def sendemail(message):
    """ Sends a mail to the required address"""
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('gmail', 'v1', credentials=creds)
    mime_message = MIMEMultipart()
    mime_message['to'] = 'hadas.c@velismedia.com'
    mime_message['subject'] = 'FinishedJob'
    mime_message.attach(MIMEText(message, 'plain'))
    raw_string = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()
    update_message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()




