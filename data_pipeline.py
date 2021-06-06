import gs_data_push
from gs_data_push import write_to_sheet


print(gs_data_push.write_to_sheet(pd.DataFrame({'Hello':[1,2,3]}),'Try'))
