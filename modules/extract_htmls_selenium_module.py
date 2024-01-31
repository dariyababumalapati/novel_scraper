from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from database_module_kgm import set_column_by_id


def initiate_driver(url: str):
    """Initialize a Chrome WebDriver and navigate to the provided URL.

    Args:
        url (str): The URL to navigate to.

    Returns:
        WebDriver: The initialized Chrome WebDriver instance.
    """
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-agent=YourCustomUserAgent")
        driver = webdriver.Chrome(options=chrome_options)

        driver.get(url)
        print("driver initiated.")

        return driver

    except Exception as e:
        print(f"Error occurred while initializing the driver: {e}")
        return None  # Return None if there's an error initializing the driver


def extraction_and_storing(driver, records: list, connection):
    for record in records:
        url = record[2]
        driver.get(url)
        id = record[0]

        try:
            content_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "w_main"))
            )

            # print(content_element)

            time.sleep(2)

            html_content = content_element.get_attribute("outerHTML")
            # print(html_content)

            set_column_by_id(connection, html_content, id)

        except Exception as e:
            print(f"Error occurred while waiting for translation: {e}")
            return None  # if there's an error waiting for translation


def scroll_to_bottom(driver, pause_time=0.5):
    # Get scroll height
    total_height = driver.execute_script("return document.body.scrollHeight")
    scroll_stroke = total_height / 10

    relay = 0

    while relay <= 10:
        relay += 1

        driver.execute_script(f"window.scrollBy(0, {scroll_stroke});")

        time.sleep(pause_time)


def copy_useful_html(driver):
    try:
        # Wait for the element to be visible and then find the element
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "w_main"))
        )

        time.sleep(3)
        # Get the HTML content of the element
        html_content = element.get_attribute("outerHTML")
        # print(html_content)

        return html_content

    except Exception as e:
        print(f"An error in copy_useful_html occurred: {e}")


# confine to the database


if __name__ == "__main__":
    print("extract_html_module.py running in main.")
