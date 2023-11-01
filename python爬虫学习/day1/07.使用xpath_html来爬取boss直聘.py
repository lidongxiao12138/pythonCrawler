from lxml import etree
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json"
    # url = "https://szkunshan.58.com/ershoufang/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0001-0130-2495-be32f9b3a2f3&ClickID=6"
    # header = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    # }
    # resopnse = requests.get(url=url, headers=header).text
    # tree = etree.HTML(resopnse)
    # list_title = tree.xpath('//h3[@class="property-content-title-name"]/text()')
    # for li in list_title:
    #     print(li)

    url = "https://www.zhipin.com/web/geek/job?query=%E7%AB%8B%E8%87%BB%E7%A7%91%E6%8A%80&city=101190400"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    resopnse = requests.get(url=url, headers=header).text
    print(resopnse)
    tree = etree.HTML(resopnse)
    list_title = tree.xpath('//span[@class="job-name"]/text()')
    for li in list_title:
        print(li)
    
