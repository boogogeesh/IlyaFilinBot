import random

import requests
from lxml import html

ENDPOINT = "https://pikabu.ru/"


def get_post_link():
    posts_type = random.choice(['hot', 'best'])
    page = requests.get(ENDPOINT + posts_type)
    print(page)
    tree = html.fromstring(page.content)
    print(tree)
