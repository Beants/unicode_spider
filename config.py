import os

URL_BASE = os.environ.get('URL_BASE', 'https://www.fuhaoku.net')
# 康熙部首
URL_KANGXI = URL_BASE + os.environ.get('URL_KANGXI', '/block/Kangxi')
# 中日韩汉字部首补充
URL_CJK_RADICALS_SUP = URL_BASE + os.environ.get('URL_CJK_RADICALS_SUP', '/block/CJK_Radicals_Sup')
# 汉文训读
URL_KANBUN = URL_BASE + os.environ.get('URL_CJK_RADICALS_SUP', '/block/Kanbun')
# 中日韩兼容表意文字
URL_CJK_COMPAT_IDEOGRAPHS = URL_BASE + os.environ.get('URL_CJK_COMPAT_IDEOGRAPHS', '/block/CJK_Compat_Ideographs')
# 中日韩兼容表意文字增补
URL_CJK_COMPAT_IDEOGRAPHS_SUP = URL_BASE + os.environ.get('URL_CJK_COMPAT_IDEOGRAPHS_SUP', '/block/CJK_Compat_Ideographs_Sup')

HEADERS = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'}
