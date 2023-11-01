from selenium import webdriver
import time
#定义无可视化界面
# from selenium.webdriver.chrome.options import Options
#----------------------------------------------------
#规避被检测
from selenium.webdriver import ChromeOptions

#无可视化页面方法
#----------------------------------------------------
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#----------------------------------------------------

#可防止selenium被检测到合并了
#----------------------------------------------------
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_argument('--headless')
option.add_argument('--disable-gpu')

#----------------------------------------------------
#如何让selenium规避掉可检测到的风险
bro = webdriver.Chrome(options=option)
bro.get('https://qzone.qq.com')
bro.switch_to.frame('login_frame')
login_btn = bro.find_element(by='id',value='switcher_plogin')
login_btn.click()
user_name = bro.find_element(by='id',value='u')
user_name.send_keys('573561243')
user_password = bro.find_element(by='id',value='p')
user_password.send_keys('Ldx12138')
login_go_btn = bro.find_element(by='id',value='login_button')
login_go_btn.click()
page_text = bro.page_source
print(page_text)
# time.sleep(20)