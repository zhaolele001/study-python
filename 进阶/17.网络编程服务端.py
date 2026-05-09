"""
    案例：网络变成入门，服务端给客户端发送消息，客户端给出回执信息
    服务端开发流程：
    1.创建服务端socket对象
    2.绑定IP和端口
    3.设置最大监听数
    4.等待客户端申请建立连接
    5.给客户端发消息
    6.接收客户端信息并打印
    7.释放资源
"""
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 0))
server_socket.listen(5)
print(1)
accept_socket, client_info = server_socket.accept()
print(2)
data = accept_socket.send(b"Welcome to the server!")
print(f"服务器端收到：，来自{client_info} 的信息{data}")
accept_socket.recv(1024).decode("utf-8")
# accept_socket.close()
