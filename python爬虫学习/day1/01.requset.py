#UA伪装，让爬虫对应的请求伪装成浏览器
import requests
if __name__ == "__main__":
    url = "https://www.sogou.com/"
    #伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    # 发起请求
    response = requests.get(url=url,headers=headers)
    # 获取响应数据
    page_text = response.text
    print(page_text)

    #储存响应数据
    with open('.sougouhtml','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬虫抓取结束！')
    
