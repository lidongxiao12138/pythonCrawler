import scrapy
from scrapyPro.items import ScrapyproItem
import pymysql
class SpidernameSpider(scrapy.Spider):
    name = "spiderName"
    start_urls = ["https://www.zhipin.com/suzhou/"]
    def parse(self, response):
        div_list = response.xpath('//*[@id="main"]/div/div[3]/ul[1]/li')
        for li in div_list:
            name = li.xpath('./div/a/div/div/p/text()')[0].extract()
            pay = li.xpath('./div/a/div/p/text()')[0].extract()
            item = ScrapyproItem()
            item['name'] = name
            item['pay'] = pay
            #提交给管道
            yield item

