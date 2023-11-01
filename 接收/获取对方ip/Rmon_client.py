import os
from socket import *
from PIL import ImageGrab
sock = socket()
sock.connect(("1.12.65.96", 1234))
if not os.path.exists('my_folder'):
    os.makedirs('my_folder')
# # 获取桌面的截图 保存在文件中
image = ImageGrab.grab()
image = image.resize((1280, 720))
image.save('my_folder/screenshot.png')
# 1 获取图片大小 发送给服务器
size = os.path.getsize('my_folder/screenshot.png')
sock.send(str(size).encode())
# # 2 接收服务器消息 是否接收完大小
ready = sock.recv(2048).decode()
print(ready)
# # 3 确认服务器已接收到大小 读取图片 发送给服务器
if ready == 'da xiao':
    file = open('my_folder/screenshot.png', 'rb')
    while True:
        data = file.read(2048)
        if not data:
            break
        sock.send(data)
    file.close()
ready = sock.recv(2048).decode()
print(ready)
if ready == 'wan cheng':
    print('文件接收完毕')
