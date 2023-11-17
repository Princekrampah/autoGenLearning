# filename: scrape_news.py

import requests
from bs4 import BeautifulSoup

def scrape_google_news(search_term):
    url = f"https://www.google.com/search?q={search_term}&tbm=nws"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news = []
    for g in soup.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('div', class_='BNeawe vvjwJb AP7Wnd').get_text()
            item = {
                "title": title,
                "link": "https://www.google.com" + link
            }
            news.append(item)
    return news

news = scrape_google_news("GPT software development")
for item in news:
    print(f"Title: {item['title']}")
    print(f"Link: {item['link']}")
    print("\n")