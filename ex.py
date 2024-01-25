from bs4 import BeautifulSoup
from bs4_module import get_page_html, prettify_content
from database_module import retrieve_table

database = "sl"

records = retrieve_table(database)

# for record in records[:10]:
#     print(record)

soup = BeautifulSoup("", "lxml")

h1_element = soup.new_tag("h1")
h1_element.string = records[0][1]
h1_element = h1_element.prettify()
print(h1_element)
# for n in range(11, 91):
#     url = f"https://www.online-novels.net/home/solo-leveling/capitolo-{n}/"
#     h_c = get_page_html(url)

#     soup = prettify_content(h_c)

#     entry_content = soup.find(class_="entry-content")

#     h1_element = entry_content.find("h1")

#     print(h1_element.text.strip())
