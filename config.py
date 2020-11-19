import os

URL_BASE = os.environ.get('URL_BASE', 'https://www.fuhaoku.net')
URL_KANGXI = URL_BASE + os.environ.get('URL_KANGXI', '/block/Kangxi')

HEADERS={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'}