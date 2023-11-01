import requests
import re
from bs4 import BeautifulSoup
if __name__ == "__main__":
    url = "https://www.chsi.com.cn/xlcx/bg.do?vcode=AWP6WYX8M8224H2X&srcid=bgcx"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.1.0.0 Safari/537.37"
    }
    page_text = requests.get(url=url,headers=header).text
    with open('.sougouhtml','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('结束！！')
