import asyncio
import time 
import aiohttp

async def requset(url):
  print("正在下载",url)
  #time属于任务同步的相关代码，无法实现异步操作法
  # time.sleep(2) 
  #使用asyncio模块，可以实现多任务的异步操作方法
  # await asyncio.sleep(2)
  #新增aiohttp异步网络请求模块的编写
  async with aiohttp.ClientSession() as session:
    #get(),post()
    #header,params/data,proxy='http://ip:prot'

    #get操作是一个耗时的操作，需要用wait挂起
    async with await session.get(url) as response:
      #text()返回字符串形式的响应数据
      #read()返回的是二进制响应的数据
      #json()返回的是json对象响应的数据
      #注意！！！！在获取响应数据之前一定要使用await进行手动挂起
      page_text = await response.text()
      print(page_text)
  print("下载完成",url)

start_time = time.time()
urls = ["baidu.con","sougou.com","douban.com"]

#任务列表：存放多个任务对象
stasks = []
for url in urls:
  c = requset(url)
  task = asyncio.ensure_future(c)
  stasks.append(task)
loop = asyncio.get_event_loop()
#如果是多任务必须将多任务列表放置在asyncio.wait 中
loop.run_until_complete(asyncio.wait(stasks))
print(time.time() - start_time)
