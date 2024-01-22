from ebooklib import epub

def replace_word(epub_path, old_word, new_word):
    book = epub.read_epub(epub_path)

    for item in book.get_items_of_type(epub.EpubItem.TEXT):
        content = item.get_content().decode('utf-8')
        new_content = content.replace(old_word, new_word)
        item.set_content(new_content.encode('utf-8'))

    with open(epub_path, 'wb') as file:
        file.write(epub.write_epub_content(book))

if __name__ == '__main__':

# Replace 'Ben' with 'Tom' in your ePub file
	replace_word('your_book.epub', 'Ben', 'Tom')
