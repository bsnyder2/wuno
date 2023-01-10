import socket

class Network:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.portNum = 5555
        self.address = (self.server, self.portNum)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            # Here we attempt to connect
            self.socket.settimeout(5.0)
            self.socket.connect(self.address)
            return self.socket.recv(2048).decode
        except socket.error as e:
            print(str(e))
            print("Could not connect")

def main():
    network = Network()

main()