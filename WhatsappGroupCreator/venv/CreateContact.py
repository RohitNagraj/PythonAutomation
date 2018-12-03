import httplib2

from googleapiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow

FLOW = OAuth2WebServerFlow(
    client_id='865447202877-5piktaelolal97db85irpiodf1o6ga64.apps.googleusercontent.com',
    client_secret='E0BZdG_rL5d5MiPxNveWSPSN',
    scope='https://www.googleapis.com/auth/contacts.readonly',
    user_agent='YOUR_APPLICATION_NAME/YOUR_APPLICATION_VERSION')


storage = Storage('client_secret.json')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  credentials = run_flow(FLOW)

http = httplib2.Http()
http = credentials.authorize(http)

people_service = build(serviceName='people', version='v1', http=http)