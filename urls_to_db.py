from bs4_module import get_ree_chn_and_url
from database_module import insert_into_urls_table


file_path = "htmls/ree_urls.html"

chapters_list = get_ree_chn_and_url(file_path)

database = "sl"
table_number = ""

# for chapter in chapters_list[5:]:
#     # print(chapter)
#     insert_into_urls_table(chapter, database, table_number)

data = ("test_title", "test_url")

insert_into_urls_table(data, database, table_number)
