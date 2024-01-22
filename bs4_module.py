from bs4 import BeautifulSoup


def get_ch_number_and_url(file_path):
    """
    Extracts chapter numbers and URLs from an HTML file.

    Parameters:
    - file_path (str): The path to the HTML file to be parsed.

    Returns:
    - list of tuples: Each tuple contains two strings,
        the chapter number and the URL.
        Returns an empty list if no items are found or in case of an error.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, "html.parser")
        chapters = []

        for li in soup.find_all("li"):
            a_tag = li.find("a")

            if a_tag and "href" in a_tag.attrs:
                chapter_title = a_tag.get_text(strip=True)
                url = a_tag["href"]
                chapters.append((chapter_title, url))

        return chapters

    except Exception as e:
        print(f"Error occurred while getting the soup: {e}")
        return []


if __name__ == "__main__":
    print("bs4_module.py running in main")

    file_path = "urls.html"

    chapters_list = get_ch_number_and_url(file_path)

    print(type(chapters_list))

    # Check the value of chapters_list
    print(chapters_list)  # This will show you the actual value

    # If chapters_list is an iterable, you can iterate over it
    if isinstance(chapters_list, (list, tuple)):
        for chapter in chapters_list:
            print(chapter)  # or insert_into_urls_table(chapter)
    else:
        print("chapters_list is not a list or tuple.")
