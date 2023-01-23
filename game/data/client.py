import socket


class Client:
    def __init__(self, host_ip, port):
        # ObieWiFi
        self.HOST_IP = host_ip
        self.PORT = port
        # IPv4
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.s.connect((self.HOST_IP, self.PORT))
        connect_msg = self.s.recv(2048).decode()
        print(connect_msg)

    def send(self, msg):
        # send data to server
        self.s.send(str.encode(msg))
        print(f"Sent \"{msg}\"")

        # receive data from server
        msg = self.s.recv(2048).decode()
        print(f"Received \"{msg}\"")