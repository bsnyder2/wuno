import socket
import _thread
import data.game


class Server:
    def __init__(self, host_ip, port):
        # ObieWiFi
        self.HOST_IP = host_ip
        self.PORT = port
        # IPv4
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.s.bind((self.HOST_IP, self.PORT))
        # accepts maximum of 4 connections
        self.s.listen(4)
        print("Server started")

        # loops to accept new connections, start on interrupt
        print("Accepting connections ... (Ctrl-C to start game)")
        self.i = 0
        try:
            while True:
                conn, addr = self.s.accept()
                # creates thread with new connection
                _thread.start_new_thread(self.connection, (conn, addr))
                print(addr, f"connected as Player", self.i)
        except KeyboardInterrupt:
            pass

    def connection(self, conn, addr):
        connection_i = self.i
        conn.send(str.encode(str(connection_i)))
        self.i += 1

        while True:
            # receive data from client
            data = conn.recv(2048)
            # if no data, disconnect
            if not data:
                print(addr, "disconnected")
                self.i -= 1
                return
            msg = data.decode()
            print(f"Received {msg} from {addr}")

            # send received data to client
            conn.sendall(str.encode(msg))
            print(f"Sent \"{msg}\" to all clients")
