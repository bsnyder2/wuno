import data.client

<<<<<<< HEAD:game/app.py
display.gui.GUI()
=======
>>>>>>> d89c934febae501e3e2c70df71307eee1641800d:game/client_app.py

def main():
    HOST_IP = "10.17.50.224"
    PORT = 50000

    # start client
    c = data.client.Client(HOST_IP, PORT)
    c.connect()
    c.send("hello")


if __name__ == "__main__":
    main()
