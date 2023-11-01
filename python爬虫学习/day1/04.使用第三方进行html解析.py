from bs4 import BeautifulSoup

if __name__ == "__main__":
    fp = open('python爬虫学习/day1/test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup.find('p',class_="story1"))
    # print(soup.find_all('p',class_="story1"))
    # print(soup.select('.story'))#层级选择器
    #使用空格表示多个层级，> 表示一个层级，通常可以使用大于号来表示
    # print(soup.select('.story > a')[0])  # 返回括号内所有元素，取第0个元素
    #string 获取标签内直系的文本内容
    #get_text() 与 text 可以获取该标签内的所有内容
    # print(soup.select('.story')[0].text)  # 标签之间的内容
    print(soup.select('.story a')[0]['href']) 

