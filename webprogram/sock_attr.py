from socket import *

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print(sockfd.getsockopt(SOL_SOCKET,SO_REUSEADDR))

sockfd.bind(('0.0.0.0', 8888))
sockfd.listen(5)

print(sockfd.family)
print(sockfd.type)
print(sockfd.getsockname())
print(sockfd.fileno())
c,addr = sockfd.accept()
print(c.getpeername())

c.recv(1024)
sockfd.close()