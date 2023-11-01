from selenium import webdriver
from lxml import etree
import time
wd = webdriver.Chrome()
wd.get("https://www.zhipin.com/suzhou/")    # 打开百度浏览器
time.sleep(5)   #等待3秒

page_text = wd.page_source
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="main"]/div/div[3]/ul[1]/li')
for li in li_list:
  name = li.xpath('./div/a/div/div/p')[0]
  print(name.text)
wd.quit()   #关闭浏览器
#爬取Boss直聘的数据列表

