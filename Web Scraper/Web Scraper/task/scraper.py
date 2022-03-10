import requests
import string
import os
from bs4 import BeautifulSoup

MAIN_URL = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page="
saved = []

n_pages = int(input())
article_type = input()
for i in range(1, n_pages + 1):
    folder_path = os.path.join(os.getcwd(), "Page_" + str(i))
    if os.access(folder_path, os.F_OK):
        for file_name in os.listdir(folder_path):
            os.remove(os.path.join(folder_path, file_name))
    else:
        os.mkdir(folder_path)
    response = requests.get(MAIN_URL + str(i))
    if response.status_code == requests.codes.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        news_articles = soup.find_all('span', {'class': 'c-meta__type'}, text=article_type)
        for news_article in news_articles:
            article = news_article.find_parent('article').find('a', {'data-track-action': 'view article'})
            article_name = article.text.translate(str.maketrans('', '', string.punctuation)).replace(" ", "_")
            saved.append(article_name)
            file = open(os.path.join(folder_path, article_name + '.txt'), 'wb')
            article_response = requests.get("https://www.nature.com" + article.get('href'))
            soup2 = BeautifulSoup(article_response.content, 'html.parser')
            page_content = soup2.find('div', {'class': 'c-article-body'}).text
            file.write(page_content.encode('utf8'))
            file.close()
    else:
        print("The URL returned {}".format(response.status_code))
print("Saved articles:\n", saved)


