import re
from pprint import pprint

import requests

base_addres = 'http://quotes.toscrape.com/'
next_page = ""
quotes = []
while True:
    addres_next_page = base_addres + next_page
    print(addres_next_page)
    page = requests.get(addres_next_page)
    text = page.text

    pp = "<span class=\"text\" itemprop=\"text\">(.*?)</span>"

    quotes += re.findall(pp, text)

    next_pages = re.findall(r"<a href=\"(.*)\">Next ", text)
    if len(next_pages) == 0:
        break
    next_page = next_pages[0]

print(len(quotes))
pprint(quotes)


