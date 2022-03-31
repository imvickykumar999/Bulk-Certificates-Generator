# https://docs.gspread.org/en/latest/api.html#gspread.spreadsheet.Spreadsheet.share

from oauth2client.service_account import ServiceAccountCredentials as sac
import gspread, pandas as pd

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

jfile = 'ideationology-lab-b60654e44e37.json'
creds = sac.from_json_keyfile_name(jfile, scope)
client = gspread.authorize(creds)

url = 'https://docs.google.com/spreadsheets/d/15s9lojXefKIbXUOp0U0Tmg5aFsiSR4G37pHR9bLQgXU/edit?resourcekey#gid=220112151'
sheet = client.open_by_url(url)

sheet_instance = sheet.get_worksheet(0)
records_data = sheet_instance.get_all_records()

df = pd.DataFrame(records_data)
df.fillna("NULL", inplace = True)
df.to_excel("HACKRIETJ-2022 (Responses).xlsx", sheet_name='HACKRIETJ-2022 (Responses)') 
