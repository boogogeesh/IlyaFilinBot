from bs4 import BeautifulSoup
import random
import requests

ENDPOINT = "https://pikabu.ru/"


def get_pikabu_post_link():
    posts_type = random.choice(['hot', 'best'])
    page = requests.get(ENDPOINT + posts_type)
    html = BeautifulSoup(page.content, "lxml")
    posts = html.find_all('a', attrs={'class': "story__title-link "}, href=True)
    post = random.choice(posts[1:])
    return post['href']

