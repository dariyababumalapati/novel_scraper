from bs4_module import get_page_html, get_ree_ul
from database_module import retrieve_urls


database = "ree"

table_number = "2"

urls = retrieve_urls(database, table_number)

for url in urls_list[:5]:
    print(url)


urls = {
    "sl_index": "https://www.online-novels.net/home/solo-leveling/",
    "ree_index": "https://www.novelhall.com/the-rise-of-the-european-emperor-17115/",
}

url = urls["ree_index"]

html_content_p = get_page_html(url)

html_content_u = get_ree_ul(html_content_p)


with open("ree_page2.html", "w", encoding="utf-8") as f:
    f.write(html_content_u)
