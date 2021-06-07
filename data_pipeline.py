import update_with_df
from update_with_df import write_to_sheet
import pandas as pd


def go(inputs, store_name):
	if store_name == 'Whole Foods':
		final_df = update_with_df.get_from_sheet('Whole Foods')
	elif store_name == 'Aldi AU':
		final_df = update_with_df.get_from_sheet('Aldi AU')
	elif store_name == 'Aldi US':
		final_df = update_with_df.get_from_sheet('Aldi US')
	elif store_name == 'Aldi UK':
		final_df = update_with_df.get_from_sheet('Aldi UK')
	elif store_name == 'Lidl':
		final_df = update_with_df.get_from_sheet('Lidl')
	return final_df

def filter_function(df, desired_ingredient):
	df["Sale Item"] = df["Sale Item"].str.lower()
	desired_ingredient = desired_ingredient.lower()
	final_df = df[df['Sale Item'].str.contains(desired_ingredient)]
	return final_df

def webify(df):
	return df.to_html()