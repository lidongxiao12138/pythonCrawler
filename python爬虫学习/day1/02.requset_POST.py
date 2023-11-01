import requests
import json
post_url = "https://fanyi.baidu.com/sug"
word = input('enter a word:')
params = {
    "kw": word
}
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
response = requests.post(url=post_url, data=params, headers=header)
print(response.json())
dic_obj = response.json()
fileName = word + ".json"
fp = open(fileName,'w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)
print('over!')
 