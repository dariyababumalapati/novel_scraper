from bs4 import BeautifulSoup, NavigableString
import requests


def get_page_html(url):
    """
    Retrieves and returns the prettified HTML content of a web page.

    This function makes an HTTP GET request to the specified URL with a set
    User-Agent header. It then parses the response content into HTML
    and returns its prettified form.

    Parameters:
    - url (str): The URL of the web page to retrieve.

    Returns:
    - str: The prettified HTML content of the page.
           Returns an empty string if there's an error at fetching or parsing.
    """
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Mobile/15E148"
        )
    }

    try:
        page = requests.get(url, headers=HEADERS)
        page.raise_for_status()
        page_doc = BeautifulSoup(page.text, "html.parser")
        return page_doc.prettify()

    except requests.exceptions.RequestException as e:
        print(f"Error occurred during HTTP request: {e}")
        return ""
    except Exception as e:
        print(f"Error occurred while parsing the HTML: {e}")
        return ""


def prettify_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    return soup


def get_ul_from_html(html_content):
    """
    Extracts and returns the prettified HTML content of the first <ul> element
    within an element with the id 'morelist' from the given HTML content.

    Parameters:
    - html_content (str): HTML content as a string.

    Returns:
    - str: The prettified HTML content of the targeted <ul> element.
           Returns an empty string if the element not found or an error occurs.
    """
    try:
        total_page = BeautifulSoup(html_content, "html.parser")
        catalog_element = total_page.find(id="morelist")

        if catalog_element is None:
            print("Element with id 'morelist' not found")
            return ""

        ul_element = catalog_element.find("ul")

        if ul_element is None:
            print("<ul> element not found within the 'morelist' element")
            return ""

        return ul_element.prettify()

    except Exception as e:
        print(f"Error occurred: {e}")
        return ""


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


def get_ree_chn_and_url(file_path):
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
                chapter_url_part = a_tag["href"]
                url = f"https://www.novelhall.com{chapter_url_part}"

                chapters.append((chapter_title, url))

        return chapters

    except Exception as e:
        print(f"Error occurred while getting the soup: {e}")
        return []


def find_p_elements_without_children(entry_content_element):
    """
    Finds and returns all <p> elements without child elements in given HTML.

    This function parses the provided HTML content and returns all <p> elements
    that contain only text and no nested tags.

    Parameters:
    - html_content (str): A string containing HTML content.

    Returns:
    - list: A list of BeautifulSoup Tag objects representing <p> elements with
            only text content.
    """
    try:
        p_novel_elements = []
        p_all_elements = entry_content_element.find_all("p")

        for p in p_all_elements:
            if len(p.contents) == 1 and isinstance(p.contents[0], NavigableString):
                p_novel_elements.append(p)

        return p_novel_elements

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def creating_html(h1_tag_text, p_tags):
    """
    Create a simple HTML structure with a main div, an H1 tag,
    and multiple P tags.

    Args:
    h1_tag_text (str): The text to be placed inside the H1 tag.
    p_tags (list of str): A list of strings,
    each representing the content of a P tag.

    Returns:
    str: A string representation of the HTML content.

    Raises:
    TypeError: If h1_tag_text is not a string or
    p_tags is not a list of strings.
    """
    try:
        # Ensure the input types are correct
        if not isinstance(h1_tag_text, str):
            raise TypeError("h1_tag_text must be a string.")
        if not all(isinstance(item, str) for item in p_tags):
            raise TypeError("All elements in p_tags must be strings.")

        # Create a BeautifulSoup object
        soup = BeautifulSoup("", "html.parser")

        # Create main div tag
        main_tag = soup.new_tag("div", id="main")

        # Create and append h1 tag
        h1_tag = soup.new_tag("h1")
        h1_tag.string = h1_tag_text  # Fixed: use assignment for string
        main_tag.append(h1_tag)

        # Append a line break
        main_tag.append(soup.new_tag("br"))

        # Append paragraph tags
        for text in p_tags:
            p_tag = soup.new_tag("p")
            p_tag.string = text
            main_tag.append(p_tag)

        # Convert the BeautifulSoup tag object to a string
        html_content = str(main_tag)

        return html_content

    except Exception as e:
        # Generic exception handling, ideally should be more specific
        print(f"An error occurred: {e}")


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
