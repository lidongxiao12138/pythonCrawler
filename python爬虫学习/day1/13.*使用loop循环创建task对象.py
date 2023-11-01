import asyncio

url = "www.baidu.com"
async def getrequset(res):
  print("正在下载。。。。",res)
  print("下载完成===",res)
  return res
c = getrequset(url)

# #创建一个loop循环对象实例
# loop = asyncio.get_event_loop()
# #将URL地址注册至对象实例中
# loop.run_until_complete(c)



# #携程对象封装至任务对象中
# #task 任务对象的使用
# loop = asyncio.get_event_loop()
# #基于loop创建一个task对象
# task = loop.create_task(c)
# print(task)
# #还没有被执行getrequset(res)这个方法

# #该方法执行task任务中的方法getrequset(res) 
# loop.run_until_complete(task)
# print(task)


# #future对象的使用
# loop = asyncio.get_event_loop()
# #将地址中的对象放置task任 务中
# task = asyncio.ensure_future(c)
# print(task)
# #将task对象使用futrue来执行
# loop.run_until_complete(task)
# print(task)



# 绑定回调
def callback_func(task):
  print(task.result())
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)
