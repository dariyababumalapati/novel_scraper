from database_module import retrieve_table, insert_into_table_column

from bs4_module import (
    # fmt: off
    get_useful_html,
    get_chapter_lines,
    creating_html
)

# fmt: on

cleaned_html_adress = {
    "database": "sl",
    "table": "sl_htmls",
    "column1": "chapter_title",
    "column2": "cleaned_html",
}

database = "sl"
urls = retrieve_table(database)

for u in urls[:4]:
    chapter_id = u[0]
    chapter_title = u[1]
    url = u[2]

    entry_content = get_useful_html(url)

    chapter_lines = get_chapter_lines(entry_content)
    cleaned_html = creating_html(chapter_title, chapter_lines)
    data_tupple = (chapter_title, cleaned_html)
    insert_into_table_column(cleaned_html_adress, data_tupple)
