import socket

#创建tcp套接字
socket = socket.socket(socket.AF_INET,\
    socket.SOCK_STREAM)

#绑定地址
socket.bind(('0.0.0.0',8886))

#设置监听
socket.listen(5)
while True:
#等待客户端连接
    print("waiting for connect ..0000.")
    try:
        connfd,addr = socket.accept()
    except KeyboardInterrupt:
        print("Server exit")
        break    
    print("Connect from",addr)  #客户端地址

    #收发消息
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("Receive message:", data.decode())
        n = connfd.send(b'Thanks your message')
        print("Send %d bytes" % n)

#关闭套接字
    connfd.close()
socket.close()

