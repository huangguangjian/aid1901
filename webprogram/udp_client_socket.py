from socket import *

#服务器地址
HOST = '176.122.12.249'
PORT = 8888
ADOR = (HOST, PORT)

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#消息收发
while True:
    data = input(">>")
    if not data:
        break
    sockfd.sendto(data.encode(), ADOR)
    msg, addr = sockfd.recvfrom(1024)
    print("From server:", msg.decode())

sockfd.close()
