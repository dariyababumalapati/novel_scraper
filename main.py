from bs4 import BeautifulSoup
from bs4_module import get_page_html, prettify_content, find_p_elements_without_children

from database_module import retrieve_table, insert_into_table_column

cleaned_html_adress = {
    "database": "sl",
    "table": "sl_htmls",
    "column": "cleaned_html",
}

database = "sl"
urls = retrieve_table(database)

for u in urls[:7]:
    url = u[2]

    h_c = get_page_html(url)

    soup = prettify_content(h_c)

    entry_content = soup.find(class_="entry-content")

    h1_element = soup.new_tag("h1")
    h1_element.string = u[1]

    all_p = entry_content.find_all("p")
    novel_all_p = find_p_elements_without_children(all_p)

    coup = BeautifulSoup("", "lxml")

    main_tag = coup.new_tag("div", id="main")
    main_tag.append(h1_element)

    for p in novel_all_p:
        main_tag.append(p)

    main_tag_pretty = main_tag.prettify()

    print("39")
    with open("htmls/main.html", "w", encoding="utf-8") as f:
        f.write(main_tag_pretty)
    insert_into_table_column(cleaned_html_adress, main_tag_pretty)
