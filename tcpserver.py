import socket

#创建tcp套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
sockfd.bind(('0.0.0.0',9988))
#设置监听
sockfd.listen(5) 
#处理客户端连接
while True:
    print('Waiting for connect.....')
    try:
        connfd,addr = sockfd.accept()
        print('Connect from',addr)
    #收发消息
    except KeyboardInterrupt:
        break
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print('Receive:',data.decode())
        n = connfd.send('Hello Kitty'.encode())
        print('Send %d bytes'%n)

            #关闭
    connfd.close()
sockfd.close()
