from bs4_module import get_ch_number_and_url
from database_module import insert_into_urls_table


file_path = "urls.html"

chapters_list = get_ch_number_and_url(file_path)

print(chapters_list)
# for chapter in chapters_list:
#     insert_into_urls_table(chapter)
