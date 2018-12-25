import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

sheets = client.open('Whatsapp Group').sheet1

phno = sheets.col_values(2)
names = sheets.col_values(1)
phno = phno[1:]
names = names[1:]