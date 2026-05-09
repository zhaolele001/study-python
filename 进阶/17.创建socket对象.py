"""


"""
import socket
#参数1：address  IAPV4/IPV6
#参数2：TCP/UDP
socketObjClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObjClient.connect(('127.0.0.1', 8888))
data = socketObjClient.recv(1024).decode("utf-8")
print(f"服务器端信息：{data}")
socketObjClient.send(b"服务器你好")




