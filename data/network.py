import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "127.0.0.1"
        self.portNum = 50012
        self.address = (self.host, self.portNum)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.settimeout(10) # will wait 10 seconds for a connection; then it times out
            self.client.connect(self.address)
            print(f"Connecting to: {self.address}")
            return self.client.recv(2048).decode("utf-8")
        except socket.error as e:
            print(e)

    def send(self, msg):
        try:
            self.client.send(str.encode(msg))
            print("Message sent successfully")
            return self.client.recv(2048).decode("utf-8")
        except socket.error as e:
            print(e)

def main():
    network = Network()
    print(network.send("This"))
    print(network.send("works"))
    
main()