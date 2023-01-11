import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.portNum = 9889
        self.address = (self.host, self.portNum)

        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            # Here we attempt to connect
            self.client.settimeout(5.0) # will wait 5 seconds for a connection; if not found, disconnects
            self.client.connect(self.address)
            return self.client.recv(2048).decode
        except socket.error as e:
            print(str(e))
            print("Could not connect")

def main():
    network = Network()
    network.connect

main()