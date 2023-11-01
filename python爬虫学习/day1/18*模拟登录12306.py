from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
#可防止selenium被检测到合并了
#----------------------------------------------------
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
# option.add_argument('--headless')
# option.add_argument('--disable-gpu')

#如何让selenium规避掉可检测到的风险
bro = webdriver.Chrome(options=option)
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
login_input = bro.find_element(by='id',value='J-userName')
login_input.send_keys('13145037933')
password_input = bro.find_element(by='id',value='J-password')
password_input.send_keys('ldx12138')
time.sleep(5)
login_btn = bro.find_element(by='id',value='J-login')
login_btn.click()
time.sleep(5)
id_card_input = bro.find_element(by='xpath',value='//*[@id="id_card"]')
id_card_input.send_keys('2112')
#发送短信验证码
verification_code = bro.find_element(by='id',value='verification_code')
verification_code.click()
time.sleep(5)
code_card_input = bro.find_element(by='xpath',value='//*[@id="code"]')
code_card_input.send_keys(input())
time.sleep(5)
code_sure = bro.find_element(by='id',value='sureClick')
code_sure.click()
print(bro.page_source)
time.sleep(20)
bro.quit()