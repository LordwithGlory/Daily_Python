import socket

class tcp_socket:
    def create_socket(self,host,port):
        # SOCK_STREAM表示是TCP连接
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect(host,port)

    def send_data(self):
        sendData='the message from client!'
        if len(sendData)>0:
            self.s.send(sendData)

    def get_data(self):
        recvData=self.s.recv(1024)
        print('the message is'+recvData)

    def close_socket(self):
        self.s.close()
        print('close socket')