from bs4 import BeautifulSoup

# Create a new BeautifulSoup object
soup = BeautifulSoup("", "html.parser")

# Create a new empty div tag
new_div = soup.new_tag("div")

# Create a new child element, for example, a paragraph <p> tag
child_p = soup.new_tag("p")
child_p.string = "This is a paragraph inside the div."

# Append the child element to the div
new_div.append(child_p)

# Create another child element, for example, a link <a> tag
child_a = soup.new_tag("a", href="https://example.com")
child_a.string = "Example Link"

# Append the second child element to the div
new_div.append(child_a)

# Append the div to the soup object
soup.append(new_div)

# Print the modified HTML
print(soup.prettify())
