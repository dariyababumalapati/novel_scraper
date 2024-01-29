from database_module_kgm import get_records

from epub_maker_kgm import EpubMaker


query = "SELECT * FROM kgm_html;"

rows = get_records(query)

# xhtml_li = [xhtml[0] for xhtml in xhtml_content]

# chapters_range = data['chapters_range']

# chapters_range = '21'


book_information = {
    "book_title": "KGM",
    "author_name": "niu",
    "language": "en",
    "image_file_path": "kgm.jpg",
    "folder_path": rows,
    "epub_file_name": "king_of_mercenaries",
    "destination_directory": "C:/Users/91833/OneDrive/Desktop/books",
}

king_of_gods = EpubMaker()
king_of_gods.make_epub(book_information)
