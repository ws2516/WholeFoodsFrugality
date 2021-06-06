import update_with_df
from update_with_df import write_to_sheet
import pandas as pd
import model
from model import aldis_us_sale

def go(inputs, store_name):
	if store_name == 'WholeFoods':
		final_df = update_with_df.get_from_sheet('Whole Foods')
	elif store_name == 'Aldi AU':
		final_df = update_with_df.get_from_sheet('Aldi AU')
	elif store_name == 'Aldi US':
		final_df = update_with_df.get_from_sheet('Aldi US')
	elif store_name == 'Aldi UK':
		final_df = update_with_df.get_from_sheet('Aldi UK')
	return final_df.to_html()

print(go('12345','Aldi US'))
