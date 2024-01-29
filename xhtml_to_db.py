from modules.database_module import retrieve_table, set_column_by_id

from modules.bs4_module import convert_html_to_xhtml


htmls_adress = {
    "database": "sl",
    "table": "sl_htmls",
}

xhtml_adress = {
    "database": "sl",
    "table": "sl_htmls",
    "column": "xhtml",
}

table_records = retrieve_table(htmls_adress)


for table_record in table_records:
    chapter_id = table_record[0]
    html = table_record[2]

    xhtml = convert_html_to_xhtml(html)

    data_set = (xhtml, chapter_id)

    set_column_by_id(xhtml_adress, data_set)
