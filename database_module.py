import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def create_connection(database_name: str):
    """
    Establishes a connection to a MySQL database.

    This function attempts to connect to a MySQL database using the provided
    database name and credentials set in environment variables. It uses a host
    address of "172.27.0.1" and the root user. The password is obtained from
    the environment variable "MYSQL_PASSWORD".

    Parameters:
    database_name (str): The name of the database to connect to.

    Returns:
    connection: A MySQL connection object if the connection is successful,
                None if the connection fails.
    """
    try:
        connection = mysql.connector.connect(
            host="192.168.1.8",
            user="root",
            password=os.environ.get("MYSQL_PASSWORD"),
            database=database_name,
        )

        if connection.is_connected():
            print("Connection is established.\n")
            return connection
        else:
            print("Connection failed.")
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# creating a connection object used throughout the functions in the module.
connection = create_connection("sl")


def insert_into_urls_table(chapter_and_url, database="sl", table_number=""):
    """
    Inserts a record into the URLs table.

    This function inserts a chapter title and URL into a specified table within
    a database. It expects a tuple containing the chapter title and URL.

    Parameters:
    connection (MySQLConnection): An active connection to the MySQL database.
    chapter_and_url (tuple): A tuple containing two elements:
        - chapter_title (str): The title of the chapter.
        - url (str): The URL corresponding to the chapter title.

    Returns:
    bool: True if the insert operation was successful, False otherwise.
    """
    try:
        connection = create_connection(database)
        cursor = connection.cursor()
        insert_query = f"""
            INSERT INTO {database}_urls{table_number} (chapter_title, url)
            VALUES (%s, %s)
        """
        cursor.execute(insert_query, chapter_and_url)
        connection.commit()
        return True

    except mysql.connector.Error as err:
        print(f"Error occurred: {err}")
        connection.rollback()
        return False

    finally:
        if cursor:
            cursor.close()


def insert_into_table_column(column_adress: dict, data):
    try:
        connection = create_connection(column_adress["database"])
        cursor = connection.cursor()
        insert_query = f"""
            INSERT INTO {column_adress['table']}
            ({column_adress['column1']}, {column_adress['column2']})
            VALUES (%s, %s)
        """
        cursor.execute(insert_query, data)
        connection.commit()
        return True

    except mysql.connector.Error as err:
        print(f"Error occurred: {err}")
        connection.rollback()
        return False

    finally:
        if cursor:
            cursor.close()


# def set_column_by_id(column_adress, html_content, chapter_id):
#     try:
#         connection = create_connection(column_adress["database"])
#         cursor = connection.cursor()

#         # update or insert data into kgm_html based on the fetched id
#         update_query = f"""
#             update {column_adress['table']} set
# {column_adress['column']} = %s where id = %s;
#             """

#         cursor.execute(update_query, (html_content, chapter_id))
#         print(f"{chapter_id} success")
#         return True

#     except mysql.connector.error as error:
#         print("error setting_data: {}".format(error))
#         connection.rollback()
#         return False

#     finally:
#         if cursor:
#             cursor.close()
#         connection.commit()
#         connection.close()


def set_column_by_id(html_content, chapter_id):
    try:
        connection = create_connection("sl")
        cursor = connection.cursor()

        # update or insert data into kgm_html based on the fetched id
        update_query = "update sl_htmls set cleaned_html = %s where id = %s;"

        cursor.execute(update_query, (html_content, chapter_id))
        print(f"{chapter_id} success")
        return True

    except mysql.connector.error as error:
        print("error setting_data: {}".format(error))
        connection.rollback()
        return False

    finally:
        if cursor:
            cursor.close()
        connection.commit()
        connection.close()


def retrieve_table(database, table_number=""):
    try:
        connection = create_connection(database)
        cursor = connection.cursor()
        insert_query = f"""
            SELECT * FROM {database}_urls{table_number}
        """
        cursor.execute(insert_query)
        records = cursor.fetchall()

        connection.commit()
        return records

    except mysql.connector.Error as err:
        print(f"Error occurred: {err}")
        connection.rollback()
        return False

    finally:
        if cursor:
            cursor.close()


def retrieve_urls(database, table_number=""):
    try:
        connection = create_connection(database)
        cursor = connection.cursor()
        insert_query = f"""
            SELECT url FROM {database}_urls{table_number}
        """
        cursor.execute(insert_query)
        records = cursor.fetchall()

        connection.commit()
        return records

    except mysql.connector.Error as err:
        print(f"Error occurred: {err}")
        connection.rollback()
        return False

    finally:
        if cursor:
            cursor.close()


if __name__ == "__main__":
    print("database_module.py running in main")
    connection = create_connection("ree")
    records = retrieve_table("sl")
    for record in records[:10]:
        print(record)
