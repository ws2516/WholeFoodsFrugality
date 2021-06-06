import update_with_df
from update_with_df import write_to_sheet
import pandas as pd
import model
from model import aldis_us_sale


print(update_with_df.write_to_sheet(aldis_us_sale.items_on_sale()))
