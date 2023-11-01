import time
from multiprocessing.dummy import Pool

star_time = time.time()
def get_page(str):
  print("正在下载：",str)
  #阻塞线程的时间
  time.sleep(2)
  print("下载成功：",str)
name_list = ["aaaa","bbbbbb","cccccc","ddddddd","ffffffff"]
#开辟4个线程池数量
pool = Pool(4)
pool.map(get_page,name_list)
end_time = time.time()
print(star_time - end_time)
