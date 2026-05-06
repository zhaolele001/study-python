"""


"""
import socket
#参数1：address  IAPV4/IPV6
#参数2：TCP/UDP
socketObjServe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketObjServe.bind(('127.0.0.1', 8888))
socketObjServe.listen(5)
accept = socketObjServe.accept()
print(accept)

socketObjClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObjClient.connect(('127.0.0.1', 8888))



