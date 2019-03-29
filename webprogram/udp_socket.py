from socket import *

#创建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

#绑定地址
server_addr = ('0.0.0.0', 8888)
sockfd.bind(server_addr)

#消息收发
while True:
    data, addr = sockfd.recvfrom(1024)   #阻塞函数 超过制定字节数的部分会丢失
    print("Receive from %s:%s"%(addr, data.decode()))
    sockfd.sendto(b'Thanks', addr)

#关闭套接字
sockfd.close()