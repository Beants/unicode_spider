import json

import requests
from bs4 import BeautifulSoup

from config import URL_BASE, HEADERS
from spider.char_spider import Char


class BlockSpider:
    """
    针对 https://www.fuhaoku.net/  中 block 的爬虫
    """
    def __init__(self, url):
        self.url = url
        self.char_list = []

        self.get_char_list()
        self.save()

    def get_char_list(self):
        """
        获取该block的所有字符
        :return:
        """
        html = requests.get(url=self.url, headers=HEADERS)
        if html.status_code != 200:
            raise ConnectionError(f'{self.url} is not reachable. the status code is {html.status_code}.')
        soup = BeautifulSoup(html.text, features="html.parser")
        char_list = soup.find_all('li', class_='char with-tooltip')
        for index, char in enumerate(char_list):
            print(f'now spider {index + 1}/{len(char_list)}:\t{char.a["href"]}')
            self.char_list.append(Char(URL_BASE + char.a['href']))

    def save(self):
        with open(f'data/{self.url.replace("https://www.fuhaoku.net/block/", "")}.json', 'w+', encoding='utf-8') as f:
            result = {i.unicode: v.unicode for i in self.char_list if (v := i.related_char)}

            f.write(json.dumps(result))
