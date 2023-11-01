from selenium import webdriver
import time
#导入动作链里的类，适用于控件拖拽等操作 
from selenium.webdriver import ActionChains
wd = webdriver.Chrome()
wd.get("https://www.zhipin.com/suzhou/")
search_input = wd.find_element(by='name',value='query')
#标签定位
search_input.send_keys('立臻科技')
#执行一组js 数据,执行页面滚动操作
# wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(5)
#点击搜索按钮
search_btn = wd.find_element(by='xpath',value='//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/button')
search_btn.click()
time.sleep(20)
wd.quit()
 

# #如果是ifrom 作用域内的控件需使用
# wd.switch_to.frame('ifrom')
# div = wd.find_element(by='',value='')

# #动作链实例化
# action = ActionChains(wd)
# #点击长按的div标签
# action.click_and_hold(div)

# for i in range(5):
#   #立即循环操作链，将控件移动5次
#   action.move_by_offset(17,0).perform()
#   time.sleep(0.5)
# #释放拖动操作
# action.release()