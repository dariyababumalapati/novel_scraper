from database_module import retrieve_table

from bs4 import BeautifulSoup

html = "<div id='main'></div>"

soup = BeautifulSoup(html, "html.parser")

html_content = soup.prettify()

adress = {
    "database": "sl",
    "table": "sl_htmls",
    "column": "raw_html",
}

records = retrieve_table(adress)

htmls = [html for record in records for html in record[2:3]]

record = records[0]
# print(len(htmls))
# for html in htmls:
#     print(html)
html_test_content = htmls[5]

example_file_path = "htmls/ex.html"

with open(example_file_path, "w", encoding="utf-8") as f:
    f.write(html_test_content)
