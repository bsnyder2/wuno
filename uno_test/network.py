import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "132.162.25.81"
        self.portNum = 5555
        self.address = (self.server, self.portNum)

        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            # Here we attempt to connect
            self.client.settimeout(5.0)
            self.client.connect(self.address)
            return self.client.recv(2048).decode
        except socket.error as e:
            print(str(e))
            print("Could not connect")

def main():
    network = Network()
    network.connect

main()