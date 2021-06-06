import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from datetime import datetime
import os

def write_to_sheet(dataframe, sheet_name):
	credentials = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
	creds = ServiceAccountCredentials.from_json_keyfile_name(credentials)
	client = gspread.authorize(creds)
	sheet = client.open("FoodSaleScrapeData").worksheet(sheet_name)
	row = [email,str(datetime.today())]
	sheet.append_row(row)
	num = next_available_row(sheet)
	return 'Done'
