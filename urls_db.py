from bs4_module import get_ree_chn_and_url
from database_module import insert_into_urls_table


file_path = "htmls/ree_urls.html"

chapters_list = get_ree_chn_and_url(file_path)

database = "ree"
table_number = "2"

for chapter in chapters_list[5:]:
    # print(chapter)
    insert_into_urls_table(chapter, database, table_number)
