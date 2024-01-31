from modules.database_module import retrieve_table
from modules.bs4_module import html_to_xhtml
from modules.epub_module import EpubMaker

# from modules.helpful_functions_module import get_file_number


file_number = 8

htmls_adress = {
    "database": "sl",
    "table": "sl_htmls",
}


table_records = retrieve_table(htmls_adress)

print(len(table_records))

xhtml_list_org = []
xhtml_list_con = []

for record in table_records[:5]:
    chapter_title = record[1]
    html = record[2]
    xhtml_org = record[3]
    xhtml_con = html_to_xhtml(html)

    chapter_data_org = (chapter_title, xhtml_org)
    chapter_data_con = (chapter_title, xhtml_con)

    xhtml_list_org.append(chapter_data_org)
    xhtml_list_con.append(chapter_data_con)

chapters_list = xhtml_list_org
epub_name = f"epubs/solo_leveling{file_number}.epub"

book_information = {
    "book_title": "Solo Leveling",
    "author_name": "Chugong",
    "language": "it",
    "image_file_path": "/mnt/c/Users/91833/OneDrive/Desktop/ree.jpeg",
    "chapter_contents": chapters_list,
    "epub_file_name": epub_name,
    "destination_directory": "/mnt/c/Users/91833/OneDrive/Desktop",
}

sl = EpubMaker()
sl.make_epub(book_information)
# print("finished")
