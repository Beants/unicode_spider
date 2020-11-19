import re

import requests
from bs4 import BeautifulSoup

from config import HEADERS, URL_BASE

BLOCK_REGEX = re.compile('<th class="prop">区段</th>\s+<td class="value">(.*?)</td>', re.S)


class Char:
    """
    对每一个unicode 字符进行爬取，并获取以下信息：
    1. 字符的block
    2，该字符的相关字符（中日韩统一表意文字）
    """
    def __init__(self, url, is_related=False):
        self.url = url
        self.unicode = url.replace('https://www.fuhaoku.net/U+', '')
        self.block = None
        self.related_char = None
        self.get_char_detail(is_related)

    def json(self):
        result = {'unicode': self.unicode}
        if self.related_char:
            result['related_char'] = self.related_char.json()
        return result

    def __repr__(self):
        return self.json().__str__()

    def get_char_detail(self, is_related=False):
        """
        1. 获取该字符的 block 信息
        2. 获取该字符的 相关字符 信息 并进行清理
        :param is_related:
        :return:
        """
        html = requests.get(url=self.url, headers=HEADERS)
        if html.status_code != 200:
            raise ConnectionError(f'{self.url} is not reachable. the status code is {html.status_code}.')

        self.block = BLOCK_REGEX.findall(html.text)
        if self.block:
            self.block = self.block[0]

        soup = BeautifulSoup(html.text, features="html.parser")
        char_related = soup.find_all('td', class_='value related')
        if not is_related:
            self.related_char = []
            for i in list(set(char_related)):

                char = Char(URL_BASE + i.a['href'], True)
                if '中日韩统一表意文字' in char.block:
                    self.related_char.append(char)
            # remove repetitive
            t_ = set()
            for i in self.related_char.copy():
                if i.unicode in t_:
                    self.related_char.remove(i)
                else:
                    t_.add(i.unicode)
            # 只保留一个
            if self.related_char:
                self.related_char = self.related_char[0]
