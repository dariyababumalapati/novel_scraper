from ebooklib import epub
import os


class EpubMaker:
    """
    A class for creating an EPUB file from HTML content.

    Attributes:
        book (epub.EpubBook): The EPUB book instance.
        chapters_list (list): A list of chapter titles added to the book.
    """

    def __init__(self):
        """
        Initializes the EpubMaker instance, setting up the necessary
        attributes for creating an EPUB file.
        """
        self.book = epub.EpubBook()
        self.book.spine = []
        self.chapters_list = []

    def add_metadata(self, book_title, author_name, language):
        """
        Adds metadata to the EPUB book.

        Args:
            book_title (str): The title of the book.
            author_name (str): The name of the author.
            language (str): The language code for the book (e.g., 'en').

        Raises:
            Exception: If an error occurs while adding metadata.
        """
        try:
            self.book.set_title(book_title)
            self.book.add_author(author_name)
            self.book.set_language(language)

        except Exception as e:
            print(f"Error adding metadata: {e}")

    def add_cover_image(self, image_file_path):
        """
        Sets the cover image for the EPUB book.

        Args:
            image_file_path (str): The file path of the cover image.

        Raises:
            FileNotFoundError: If the specified image file does not exist.
            Exception: For any other errors that occur.
        """
        try:
            if not os.path.isfile(image_file_path):
                raise FileNotFoundError(
                    f""" Image file not found: {image_file_path}""",
                )

            with open(image_file_path, "rb") as f:
                self.book.set_cover("image.jpg", f.read())

        except Exception as e:
            print(f"Error setting cover image: {e}")

    def add_chapters(self, chapter_data_list, language):
        """
        Adds chapters to the EPUB book.

        Args:
            chapter_data_list (list of tuples): A list where each
            tuple contains the chapter title and the chapter XHTML content.
            language (str): The language code of the chapters (e.g., 'en').

        Raises:
            ValueError: If chapter_data_list does not contain
            tuples with exactly 2 elements.
            Exception: If an error occurs while adding chapters.
        """
        # Validate chapter_data_list structure
        for item in chapter_data_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError(
                    """Each item in chapter_data_list must be
                    a tuple with exactly 2 elements (title, xhtml)."""
                )

        try:
            for chapter_data in chapter_data_list:
                chapter_title, chapter_xhtml = chapter_data
                c = epub.EpubHtml(
                    title=chapter_title, file_name=chapter_title, lang=language
                )
                c.content = chapter_xhtml
                self.book.add_item(c)
                self.book.spine.append(c)
                self.chapters_list.append(chapter_title)

                print(f"{chapter_title} added.")

        except Exception as e:
            print(f"Error adding chapters: {e}")

    def add_table_of_contents(self):
        """
        Adds a table of contents to the EPUB book.

        Raises:
            Exception: If an error occurs while adding the table of contents.
        """
        try:
            self.book.toc = (
                epub.Link("cover.xhtml", "Cover", "cover"),
                (
                    epub.Section("Chapters"),
                    [
                        epub.Link(f"{title}.xhtml", title, title)
                        for title in self.chapters_list
                    ],
                ),
            )

        except Exception as e:
            print(f"Error adding table of contents: {e}")

    def create_epub_file(self, destination_folder, epub_file_name):
        """
        Creates the EPUB file on disk.

        Args:
            epub_file_name (str): The filename for the EPUB file.

        Raises:
            Exception: If an error occurs during EPUB file creation.
        """
        try:
            epub_file_path = f"{destination_folder}/{epub_file_name}"
            epub.write_epub(epub_file_path, self.book, {})

        except Exception as e:
            print(f"Error creating epub file: {e}")

        else:
            print(f"Epub file created successfully: {epub_file_name}")

    def make_epub(self, book_info):
        """
        Creates an EPUB file from provided book information in a single action.

        Args:
            book_info (dict): A dictionary containing all necessary information
            to create the EPUB file, including the title, author, language,
            cover image path, chapter contents, and file name.

        Raises:
            Exception: If an error occurs at any step of EPUB creation process.
        """
        try:
            self.add_metadata(
                book_info.get("book_title"),
                book_info.get("author_name"),
                book_info.get("language"),
            )
            self.add_cover_image(book_info.get("image_file_path"))
            self.add_chapters(
                book_info.get("chapter_contents"), book_info.get("language")
            )
            self.add_table_of_contents()
            self.create_epub_file(book_info.get("epub_file_name"))

        except Exception as e:
            print(f"Error making epub: {e}")


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
