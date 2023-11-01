import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://www.qidian.com/book/1037725135/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    resopnse = requests.get(url=url, headers=header)
    soup = BeautifulSoup(resopnse.text, 'lxml')
    title_list = soup.select('.catalog-volume > ul > li > a')
    titleArr = []
    titleArrUrl = []
    for list in title_list:
        title = list.string
        title_url = 'https:'+list['href']
        titleArr.append(list.string)
        titleArrUrl.append(title_url)
    resopnse1 = requests.get(url=titleArrUrl[0],headers=header)
    soup1 = BeautifulSoup(resopnse1.text, 'lxml')
    content_list = soup1.select('.text-s-gray-500 mt-4px text-bo4 flex items-center flex-wrap')
    soup1_text = str(soup1.select('main',id="c-762480796")) 
    soup2 = BeautifulSoup(soup1_text, 'lxml')
    soup2_list = soup2.select('p')
    all_text = ""
    for i in range(1,len(soup2_list)):
        all_text += soup2_list[i].text+"\n"
    print(all_text)
    with open(titleArr[0].text,'w',encoding='utf-8') as fp:
        fp.write(all_text)
    