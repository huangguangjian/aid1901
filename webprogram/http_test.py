from socket import * 
#创建套接字
s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(5)

#接收浏览器请求
c,addr = s.accept()
print("Connect from", addr)

data = c.recv(4096)
print(data)

#组织http响应格式
data = '''HTTP/1.1 200 OK
Content-Encoding:utf-8
Content-Type: text/html

<h1>hello world ,good morning<h1>
'''
c.send(data.encode())
# c.send(b"hello world")

c.close()
s.close()
