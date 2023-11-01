from lxml import etree

if __name__=="__main__":
  tree = etree.parse("python爬虫学习/day1/test.html")
  #/ 表示一个层级， // 表示多个层级 //div 可以检索所有div层级
  # r = tree.xpath('/html/head/title')
  # r = tree.xpath('//p[@class = "story1"]/text()')[0]
  r = len(tree.xpath ('//p/a/@href'))
  print(r) 