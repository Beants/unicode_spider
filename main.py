from spider.block_spider import BlockSpider
from config import URL_KANGXI

if __name__ == '__main__':
    spider = BlockSpider(URL_KANGXI)

    for i in spider.char_list:
        print(i.__dict__)
