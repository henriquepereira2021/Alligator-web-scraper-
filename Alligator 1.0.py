from bs4 import BeautifulSoup
import requests
import re

link = input("Insert the URL: ")

html = requests.get(link).content

soup = BeautifulSoup(html, 'html.parser')

domain_reuters = link.find("reuters.com")

text = []

if domain_reuters > -1:

    article = soup.find('div', class_="article-body__content__17Yit paywall-article")

    paragraphs = article.find_all('p', class_="text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__base__22dCE body__large_body__FV5_X article-body__element__2p5pI")

    for i in paragraphs:
        body = i.get_text()
        text.append(body)
        text.append('\n')
        text.append('\n')

    text_str = ''.join((str(d) for d in text))

    print()
    print(text_str)