import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from datetime import datetime
import os

def write_to_sheet(email):
	credentials = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
	creds = ServiceAccountCredentials.from_json_keyfile_name(credentials)
	sheet = client.open("FoodSaleScrapeSignUp").sheet1
	row = [email,str(datetime.today())]
	sheet.append_row(row)
	num = next_available_row(sheet)
	return int(num)

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)-2)
