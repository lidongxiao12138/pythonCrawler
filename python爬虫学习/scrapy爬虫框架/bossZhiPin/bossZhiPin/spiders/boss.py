import scrapy


class BossSpider(scrapy.Spider):
    name = "boss"
    start_urls = ["https://www.zhipin.com/web/geek/job?query=立臻科技&city=101190400"]
    # start_urls = ["https://www.zhipin.com/suzhou/"]
    def parse(self, response):
        li_list = response.xpath('//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[3]/ul')
        # li_list = response.xpath('//*[@id="main"]/div/div[3]/ul[1]/li')
        print(li_list)
        for li in li_list:
            name = li.xpath('./div[1]/a/div[1]/span[1]/text()')
            print(name)
