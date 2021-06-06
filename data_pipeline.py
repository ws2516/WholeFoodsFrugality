import update_with_df
from update_with_df import write_to_sheet


print(update_with_df.write_to_sheet(pd.DataFrame({'Hello':[1,2,3]}),'Try'))
