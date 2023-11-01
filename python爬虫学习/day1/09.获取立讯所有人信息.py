import requests
import datetime
url_login = "https://lzhr.luxsan-ict.com:8443/jeecg-boot/sys/loginSkipVerification"
data_login = '{"username":"75301150"}'
head_login = {
    "Content-Type": "application/json;charset=UTF-8"
}
#创建cookie 对象
session = requests.session()
response_login = session.post(
    url=url_login, data=data_login, headers=head_login).json()
print(response_login["message"])
login_token = response_login["result"]["token"]
# 时间戳
now = datetime.datetime.now()
timestamp = now.timestamp()
cpf02 = "李东"
url = "https://lzhr.luxsan-ict.com:8443/jeecg-boot/att/attEmployee/list?_t=" + \
    str(timestamp)+"&cpf02="+cpf02 + \
    "&column=createTime&order=desc&field=id,,cpf01,cpf02,cpf03,werks,cpf14,ostext,sstext,cpf37&pageNo=1&pageSize=10"
header = {
    "X-Access-Token": login_token
}
response = session.get(url=url, headers=header).json()
# print(response)
datalist = response["result"]["records"]
for text in datalist:
    print("当前角色工号：", text["id"], "\n当前角色部门：", text["ostext"],
          "\n当前角色姓名：", text["cpf02"], "\n-----------")
