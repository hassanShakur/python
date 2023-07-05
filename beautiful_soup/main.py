from bs4 import BeautifulSoup

with open("./beautiful_soup/test.html") as html:
    content = html.read()

the_soup = BeautifulSoup(content, "html.parser")

print(the_soup.prettify())

all_anchors = the_soup.find_all(name="a")
first_anchor = the_soup.find(name="a")
a_href = first_anchor.get("href")
a_text = first_anchor.getText()


by_class = the_soup.find_all(class_="my-class")

by_css_selector = the_soup.select_one(selector="body div .my-class")
