import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project FASO-12400f1c27b0.json',scope)

gc = gspread.authorize(credentials)


wks = gc.open('Protectart').sheet1
def donnee() : 
    date = time.strftime('%d/%m/%y',time.localtime())
    wks.append_row([ date,'1'])
