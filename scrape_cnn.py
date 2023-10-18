#!/usr/bin/python3

from requests_html import HTMLSession
from sys import argv, exit

session = HTMLSession()

if len(argv) == 2:
    url = argv[1]
else:
    print(f"Usage: {argv[0]} <url>")
    exit

header = {
    "User-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
}

try:
    response = session.get(url, headers=header).html
    title = response.find('h1.headline__text')[0].text
    author = response.find('span.byline__name')[0].text
    last_updated = response.find('div.timestamp')[0].text
    content = response.find('p.paragraph.inline-placeholder')


    print(f"Article Title: {title}")
    print(f"Updated Date: {last_updated}")
    print(f"Author: {author}")
    print()

    for paragraph in content:
        print(paragraph.text)
except:
    print("Invalid url")
