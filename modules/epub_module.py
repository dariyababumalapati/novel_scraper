from ebooklib import epub


class EpubMaker:
    """Creating an epub file for the novel with the html files."""

    def __init__(self):
        """
        Initialize attributes to making epub file
        """
        self.book = epub.EpubBook()
        self.book.spine = []
        self.chapters_list = []

    def add_metadata(self, book_title, author_name, language):
        """
        Add meta data for the book.

        Args:
            book_title (string): Title of the data
            author_name (string): Author's name
            language (string): Language of the book
        """
        self.book.set_title(book_title)
        self.book.add_author(author_name)
        self.book.set_language(language)

    def add_cover_image(self, image_file_path):
        """
        Set the cover image for the book

        Args:
            image_file (file path): file path of the image
        """
        with open(image_file_path, "rb") as f:
            self.book.set_cover("image.jpg", f.read())

    def add_chapters(self, chapter_data_list: list, language: str):
        """
        Adding chapters to the epub book

        Args:
            folder_path (file path): file path of the folder
            language(string): select language like 'en', 'it', etc
        """
        # chapters_file_list = sorted(os.listdir(folder_path))

        for chapter_data in chapter_data_list:
            chapter_title = chapter_data[0]
            chapter_xhtml = chapter_data[1]
            # filename = f'{folder_path}/{file}'
            file_title = chapter_title

            # with open(filename, 'r', encoding='utf-8') as f:
            # fmt: off
            c = epub.EpubHtml(
                title=file_title, file_name=file_title, lang=language
            )
            # fmt: on
            c.content = chapter_xhtml
            self.book.add_item(c)
            self.book.spine.append(c)
            self.chapters_list.append(f"{file_title}")

    def add_table_of_contents(self):
        """Adding the table of contents"""

        self.book.toc = (
            epub.Link("cover.xhtml", "Cover", "cover"),
            (
                epub.Section("HTML Files"),
                [epub.Link(file, file, file) for file in self.chapters_list],
            ),
        )

    def create_epub_file(self, epub_file_name):
        """
        Last step to making the epub file of the book by writing to the file

        Args:
            epub_file_name (string): Choose the name for the epub file
            destination_directory (file_path): choose the destination location
            of the output file.
        """
        epub.write_epub(f"{epub_file_name}.epub", self.book, {})

    def make_epub(self, book_info: dict):
        """
        A method that performs all the methods in this MakeEpub class and
        makes an epub file of a novel in one single action.

        Args:
            book_info (dict): A dictionary containing all the information
            needed to create an epub file of a novel.
        """
        self.add_metadata(
            book_info["book_title"],
            book_info["author_name"],
            book_info["language"],
        )
        self.add_cover_image(book_info["image_file_path"])
        self.add_chapters(book_info["folder_path"], book_info["language"])
        self.add_table_of_contents()
        self.create_epub_file(
            f"""
            {book_info["destination_directory"]}/{book_info["epub_file_name"]}
            """
        )


if __name__ == "__main__":
    print("epub_maker.py running in main.")

    # book_info = {
    #     "book_title": "KOG",
    #     "author_name": "Fast Food Restaurant",
    #     "language": "en",
    #     "image_file_path": "cover.jpg",
    #     "folder_path": "xhtml_files",
    #     "epub_file_name": "King Of Gods.epub",
    #     }
    print("ok")
