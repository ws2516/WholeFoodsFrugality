import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from datetime import datetime
import os

def write_to_sheet(dataframe, sheet_name):
	credentials = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
	creds = ServiceAccountCredentials.from_json_keyfile_name(credentials)
	client = gspread.authorize(creds)
	sheet = client.open("FoodScrapeData").worksheet(sheet_name)
	sheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
	return 'Done'

def get_from_sheet(sheet_name):
	credentials = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
	creds = ServiceAccountCredentials.from_json_keyfile_name(credentials)
	client = gspread.authorize(creds)
	sheet = client.open("FoodScrapeData").worksheet(sheet_name)
	table = sheet.get_all_values()
	headers = table.pop(0)
	return pd.DataFrame(table, columns=headers)

