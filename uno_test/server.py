import socket
from _thread import *
import sys

class Server:

    def __init__(self):
        # This is our local server (only people that are connected to ObieWiFi)
        self.server = "10.17.3.65"
        # This allows us to send and receive data
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.portNum = 5555

        try:
            self.socket.bind((self.server, self.portNum))
        except socket.error as e:
            str(e)

        # Connects to four people
        self.socket.listen(4)
        print("Waiting for a connection...Starting Server")

    def thread(self, connection):
        reply = ""
        while True:
            try:
                data = connection.recv(2048) # Receiving data
                reply = data.decode("utf-8")

                if not data:
                    print("Server Disconnected")
                    break
                else:
                    print("Received: ", reply)
                    print("Sending: ", reply)

                connection.sendall(str.encode(reply))

            except:
                break

    # This method lets us search for a connection
    def getConnection(self):
        while True:
            connection, address = self.socket.accept()
            print("Connecting to: ", address)
            srvr = Server()
            start_new_thread(srvr.thread(connection))

def main():
    server = Server()
    print(server.getConnection)

main()
