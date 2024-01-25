from database_module import retrieve_urls


database = "ree"

table_number = "2"

urls_list = retrieve_urls(database, table_number)

for url in urls_list[:5]:
    print(url[0])
