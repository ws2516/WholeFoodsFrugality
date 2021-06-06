import update_with_df
from update_with_df import write_to_sheet
import pandas as pd
import model
from model import combination_file


print(update_with_df.write_to_sheet(combination_file.go('1234','Whole Foods')))
