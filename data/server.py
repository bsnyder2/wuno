import socket
from _thread import *

HOST = "localhost"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try: 
    client.bind((HOST, PORT))
    client.listen(4)
    print("Waiting for connection...connected")
except socket.error as e:
    print(e)

def thread(connection):
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
                print(f"Sending: {msg}")
        except:
            break
    print("Connection Lost")
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()
        

while True:
    conn, addr = client.accept()
    print(f"Connecting to: {addr}")
    start_new_thread(thread, (conn,))