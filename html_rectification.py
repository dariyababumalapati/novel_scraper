from modules.bs4_module import html_to_xhtml
from modules.database_module import retrieve_table
from modules.helpful_functions_module import save_html

htmls_adress = {
    "database": "sl",
    "table": "sl_htmls",
}


table_records = retrieve_table(htmls_adress)

html_sample = table_records[3][2]

xhtml_sample = table_records[3][3]

# print(html_sample)

# print(xhtml_sample)

html_file_path = "htmls/html_rec.html"
xhtml_file_path1 = "htmls/xhtml_rec.html"
xhtml_file_path2 = "htmls/xhtml_rec2.html"

save_html(html_file_path, html_sample)
save_html(xhtml_file_path1, xhtml_sample)
xht = html_to_xhtml(html_sample)
save_html(xhtml_file_path2, xht)
