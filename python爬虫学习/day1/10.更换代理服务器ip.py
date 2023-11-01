import requests
# url = "https://www.baidu.com/s?wd=ip"
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=84053098_3_dg&wd=ip&oq=%25E4%25BB%25A3%25E7%2590%2586ip&rsv_pq=eae5c32700008e64&rsv_t=3213kCaEkyZwJJh50CvhnbsypItQzs5Iq%2BUeuCrvZ3Yj9mY%2Fjjd9Zg84DHQWMg%2FsGKxf7A&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_btype=t&inputT=1499&rsv_sug3=8&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&rsv_sug4=3268"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}
page_text = requests.get(url=url,headers=header,proxies={"http":"http://182.140.244.163:8118"}).text
with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
