import socket

class Server:

    def __init__(self):
        # This is our local server
        self.svr = "10.17.3.65"
        # This allows us to send and receive data
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)