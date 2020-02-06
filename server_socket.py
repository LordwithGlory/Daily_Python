import socket

class ser_socket:
    def create_socket(self,port,queuenum):
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 将socket绑定到地址,gethostname是服务器的地址
        hostname=socket.gethostname()
        self.s.bind(socket.gethostbyname(hostname),port)
        # 队列中累计的最大的连接请求数量,默认是5
        self.s.listen(queuenum)

    def listen_server(self):
        (clientsocket,_)=self.s.accept()
        while True:
            recvData=clientsocket.recv(1024)
            if len(recvData)>0:
                clientsocket.send('response')
            elif len(recvData)==0:
                clientsocket.close()
                print('socket end!!!')
                break

    def close_socket(self):
        self.s.close()

# print(socket.gethostname())