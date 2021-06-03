import get_nearby_names
import sales_page_scraper

def go(inputs):
    whole_foods_names = get_nearby_names.on_input_run(inputs)
    names_list = [i.split('-')[0] for i in whole_foods_names]
    final_df = sales_page_scraper.all_together(names_list)
    return final_df