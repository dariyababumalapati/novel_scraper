from database_module import retrieve_table, insert_into_table_column

from bs4 import BeautifulSoup

html = "<div id='main'></div>"

soup = BeautifulSoup(html, "html.parser")

html_content = soup.prettify()

cleaned_html_adress = {
    "database": "sl",
    "table": "sl_htmls",
    "column": "raw_html",
}

insert_into_table_column(cleaned_html_adress, html_content)
