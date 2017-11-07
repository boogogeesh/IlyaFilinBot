from bs4 import BeautifulSoup
import random
import requests

ENDPOINT = "https://pikabu.ru/"


def get_pikabu_post_link():
    http_proxy = "http://10.10.1.10:3128"
    https_proxy = "https://10.10.1.11:1080"
    ftp_proxy = "ftp://10.10.1.10:3128"

    proxy_dict = {
        "http": http_proxy,
        "https": https_proxy,
        "ftp": ftp_proxy
    }

    posts_type = random.choice(['hot', 'best'])
    page = requests.get(ENDPOINT + posts_type, proxies=proxy_dict)
    html = BeautifulSoup(page.content, "lxml")
    posts = html.find_all('a', attrs={'class': "story__title-link "}, href=True)
    post = random.choice(posts[1:])
    return post['href'] if len(posts) != 0 else ""

