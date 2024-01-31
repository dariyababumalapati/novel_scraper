from modules.database_module import retrieve_table
from modules.epub_module import EpubMaker


htmls_adress = {
    "database": "sl",
    "table": "sl_htmls",
}


table_records = retrieve_table(htmls_adress)

chapter_data_list = [(record[1], record[3]) for record in table_records]


book_information = {
    "book_title": "Solo Leveling",
    "author_name": "Chugong",
    "language": "it",
    "image_file_path": "/mnt/c/Users/91833/OneDrive/Desktop/ree.jpeg",
    "chapter_contents": chapter_data_list,
    "epub_file_name": "solo_leveling.epub",
    "destination_directory": "/mnt/c/Users/91833/OneDrive/Desktop/books/sl",
}

sl = EpubMaker()
sl.make_epub(book_information)
