import socket
from _thread import *

HOST = "localhost"
PORT = 9119

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This lets us reuse the same address without having to wait
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

try: 
    sock.bind((HOST, PORT))
    sock.listen(4)
    print("Waiting for connection...connected")
except socket.error as e:
    print(e)

def thread(connection):
    connection.send(str.encode("Connection successful"))
    msg = ""
    while True:
        try:
            data = connection.recv(2048)
            msg = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print(f"Received: {msg}")
        except:
            break
    print("Connection Lost")
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()
        
while True:
    conn, addr = sock.accept()
    print(f"Connecting to: {addr}")
    start_new_thread(thread, (conn,))