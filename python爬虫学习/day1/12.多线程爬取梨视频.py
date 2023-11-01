import requests
from lxml import etree
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}

url = 'https://www.pearvideo.com/category_1'

page_text = requests.get(url=url, headers=header).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
for li in li_list:
    detail_url = "https://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]+".mp4"
    # print(detail_url, name)
    detail_page_text = requests.get(url=detail_url,headers=header).text
    print(detail_page_text)
    #从详情页解析视频
    
    
