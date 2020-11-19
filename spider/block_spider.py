import json

import requests
from bs4 import BeautifulSoup

from config import URL_BASE, HEADERS
from spider.char_spider import Char


class BlockSpider:
    def __init__(self, url):
        self.url = url
        self.char_list = []

        self.get_char_list()
        self.save()

    def get_char_list(self):
        html = requests.get(url=self.url, headers=HEADERS)
        if html.status_code != 200:
            raise ConnectionError(f'{self.url} is not reachable. the status code is {html.status_code}.')
        # print(html.text)
        soup = BeautifulSoup(html.text, features="html.parser")
        char_list = soup.find_all('li', class_='char with-tooltip')
        for index, char in enumerate(char_list):
            print(f'now spider {index + 1}/{len(char_list)}:\t{char.a["href"]}')
            self.char_list.append(Char(URL_BASE + char.a['href']))

    def save(self):
        with open('data/kangxi.json', 'w+', encoding='utf-8') as f:
            f.write(json.dumps({'data': self.char_list}))
