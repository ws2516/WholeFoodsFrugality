import update_with_df
from update_with_df import write_to_sheet
import pandas as pd
import model
from model import aldis_us_sale
from model import aldis_au_sale
from model import whole_foods_sale
from model import lidls_sale

def update_all():
	update_with_df.write_to_sheet(whole_foods_sale.items_on_sale(),'Whole Foods')
	update_with_df.write_to_sheet(aldis_au_sale.items_on_sale(),'Aldi AU')
	update_with_df.write_to_sheet(aldis_us_sale.items_on_sale(),'Aldi US')
	update_with_df.write_to_sheet(aldis_us_sale.items_on_sale(),'Aldi UK')
	update_with_df.write_to_sheet(lidls_sale.items_on_sale(),'Lidl')
	return 'Done'

print(update_all())
