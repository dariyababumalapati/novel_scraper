from bs4 import BeautifulSoup


def create_html_file(html_content, file_path):
    """
    Create an HTML file with formatted content.

    Args:
    - html_content (str): HTML content as a string.
    - file_path (str): File path to save the HTML content.

    Returns:
    - None
    """
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        formatted_html = soup.prettify()

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(formatted_html)

        print(f"{file_path} created.")

    except Exception as e:
        print(f"Error occurred while creating HTML file: {e}")


file_path = "urls_raw.html"


with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

print(html_content)
create_html_file(html_content, "urls.html")
