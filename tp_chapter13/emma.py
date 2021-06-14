## 
# Copy the content of book Emma from "https://github.com/AllenDowney/ThinkPython2/blob/master/code/emma.txt"
# in a .txt file using BeautifulSoup library
#
from bs4 import BeautifulSoup
import requests

# Store the content of the web page in a variable
page = requests.get("https://github.com/AllenDowney/ThinkPython2/blob/master/code/emma.txt")
page_content = page.content

# Keep accessing to nested tags until <body> tag and then
# access to the tags <td> containing the text of the book
soup = BeautifulSoup(page_content, "html.parser")
html = list(soup.children)[3]
body = list(html.children)[3]
text = body.find_all("td", class_="blob-code-inner")

# For each <td> tag, get the text and join it to a str variable
text_str = "".join(line.get_text() for line in text)

## Create a new text file called "emma.txt" and write the content of text_string on it
with open("emma.txt", "w", encoding='utf-8-sig') as fl:
    fl.write(text_str)
