import requests
from lxml import etree
from LDXHTTPDomeCode import YdmVerify

def getCodeText(path):
    with open (path,'rb') as f:
        s = f.read()
    result = YdmVerify.common_verify(self=YdmVerify,image=s,verify_type="10110")
    print("result====",result)
    return result

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

urls = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"

page_text = requests.get(url=urls, headers=header).text
tree = etree.HTML(page_text)
code_img_src = "https://so.gushiwen.cn" + tree.xpath('//*[@id="imgCode"]/@src')[0]
image_data = requests.get(url=code_img_src, headers=header).content
with open('./code.jpg', 'wb')as fp:
    fp.write(image_data)

code_text = getCodeText("./code.jpg")
