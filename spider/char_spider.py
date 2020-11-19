import re

import requests
from bs4 import BeautifulSoup

from config import HEADERS, URL_BASE

BLOCK_REGEX = re.compile('<th class="prop">区段</th>\s+<td class="value">(.*?)</td>', re.S)


class Char:
    def __init__(self, url, is_related=False):
        self.url = url
        self.block = None
        self.related_char = None
        self.get_char_detail(is_related)

    def __repr__(self):
        return self.__dict__.__str__()

    def get_char_detail(self, is_related=False):
        html = requests.get(url=self.url, headers=HEADERS)
        if html.status_code != 200:
            raise ConnectionError(f'{self.url} is not reachable. the status code is {html.status_code}.')
        # print(html.text)
        soup = BeautifulSoup(html.text, features="html.parser")
        char_related = soup.find_all('td', class_='value related')
        self.block = BLOCK_REGEX.findall(html.text)
        if self.block:
            self.block = self.block[0]
        if not is_related:
            self.related_char = []
            for i in char_related:
                char = Char(URL_BASE + i.a['href'], True)
                if '中日韩统一表意文字' in char.block:
                    self.related_char.append(char)
