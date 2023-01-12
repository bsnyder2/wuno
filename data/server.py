import socket
from _thread import *
import datetime

class Server:

    def __init__(self):
        self.host = "localhost"
        # This allows us to send and receive data
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.portNum = 9889

        try:
            # This links the socket to the address which is the server and the port number
            self.client.bind((self.host, self.portNum)) 
            # Connects to four people
            self.client.listen(4)
            print("Waiting for a connection...Starting Server")
        except socket.error as e:
            print(str(e))

    # Threading lets us handle all the connections so we don't need to call getConnection several times
    def thread(self, connection):
        currentServerTime = "%s"%datetime.now()
        connection.send(str.encode("Connected"))
        connection.send(currentServerTime.encode())

        reply = ""
        while True:
            try:
                data = connection.recv(2048) # Receives data in the form of bytes
                reply = data.decode("utf-8") # Here we turn the data into a string format

                if not data:
                    print("Server Disconnected")
                    break
                else:
                    print(f"Received:  {reply}")
                    print(f"Sending: {reply}")

                connection.sendall(str.encode(reply)) # This sends the data to the client

            except:
                break

        print("Lost Connection")
        connection.close()

    # This method lets us search for a connection
    def getConnection(self):
        while True:
            connection, address = self.client.accept() # Here we accept a connection
            print(f"Connecting to: {address}")
            start_new_thread(self.thread, (connection,))

    def endConnection(self):
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close

def main():
    server = Server()
    server.getConnection
    server.endConnection

main()
