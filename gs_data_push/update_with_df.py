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
	sheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
	return 'Done'

print(write_to_sheet(pd.DataFrame({'Hello':[1,2,3]}),'Try'))