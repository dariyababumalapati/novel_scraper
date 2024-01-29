from modules.database_module import retrieve_table


xhtml_adress = {
    "database": "sl",
    "table": "sl_htmls",
    "column": "xhtml",
}


x_table_records = retrieve_table(xhtml_adress)

xhtmls = [xhtml for element in x_table_records for xhtml in element[3:]]

index = 132

print(xhtmls[index])
