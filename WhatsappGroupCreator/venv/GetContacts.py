import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.txt', scope)
client = gspread.authorize(credentials)

sheets = client.open('Whatsapp Group').sheet1

details = sheets.col_values(2)
details = details[1:]
print(details)