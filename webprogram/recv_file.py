from socket import * 
s = socket()
s.bind(('0.0.0.0', 8889))
s.listen()
c, addr = s.accept()
print("Connect from ", addr)
data = c.recv(1024)
f = open(data.decode(), 'wb')
# f = open('dog.jpg','wb')
while True:
    data = c.recv(1024)  # 当连接的另一端断开连接会返回空字符串
    if data == b"##":
        break
    f.write(data)
c.send(b"Receive end")    
f.close()
c.close()
s.close()    