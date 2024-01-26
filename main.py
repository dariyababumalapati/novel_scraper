from database_module import retrieve_table, set_column_by_id

from bs4_module import (
    # fmt: off
    get_useful_html,
    get_chapter_lines,
    creating_html
)

# fmt: on

adress = {
    "database": "sl",
    "table": "sl_htmls",
    "column": "html",
}


urls = retrieve_table(adress)

for u in urls[:50]:
    chapter_id = u[0]
    chapter_title = u[1]
    url = u[2]

    entry_content = get_useful_html(url)

    chapter_lines = get_chapter_lines(entry_content)
    html = creating_html(chapter_title, chapter_lines)
    # data_tupple = (chapter_title, html)
    data_tupple = (html, chapter_id)
    set_column_by_id(adress, data_tupple)
