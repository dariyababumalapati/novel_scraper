from modules.database_module import retrieve_table

from modules.bs4_module import convert_html_to_xhtml


htmls_adress = {
    "database": "sl",
    "table": "sl_htmls",
}


table_records = retrieve_table(htmls_adress)

htmls = [html for element in table_records for html in element[2:3]]

# print(htmls[100])
xhtmls = []

for table_record in table_records[:2]:
    chapter_id = table_record[0]
    html = table_record[2]
    with open("htmls/ex2.html", "w", encoding="utf-8") as f:
        f.write(html)

    xhtml = convert_html_to_xhtml(html)

    with open("htmls/ex.html", "w", encoding="utf-8") as f:
        f.write(xhtml)
