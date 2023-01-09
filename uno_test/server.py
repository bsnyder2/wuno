import socket
from _thread import *

class Server:

    def __init__(self):
        # This is our local server (only people that are connected to ObieWiFi)
        self.server = "10.17.3.65"
        # This allows us to send and receive data
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.portNum = 5555

        try:
            # This links the socket to the address which is the server and the port number
            self.socket.bind((self.server, self.portNum)) 
        except socket.error as e:
            print(str(e))

        # Connects to four people
        self.socket.listen(4)
        print("Waiting for a connection...Starting Server")

    # Threading lets us decrease the amount of tasks the system has to do
    def thread(self, connection):
        reply = ""
        while True:
            try:
                data = connection.recv(2048) # Receives data in the form of bytes
                reply = data.decode("utf-8") # Here we turn the data into a string format

                if not data:
                    print("Server Disconnected")
                    break
                else:
                    print("Received: ", reply)
                    print("Sending: ", reply)

                connection.sendall(str.encode(reply)) # This sends the data to the socket

            except:
                break

    # This method lets us search for a connection
    def getConnection(self):
        while True:
            connection, address = self.socket.accept() # Here we accept a connection
            print("Connecting to: ", address)
            start_new_thread(self.thread(connection))

    def endConnection(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close

def main():
    server = Server()
    print(server.getConnection)
    server.endConnection

main()
