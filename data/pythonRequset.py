import requests
url = "https://www.zhipin.com"


res = requests.get(url)
print(res.text)
