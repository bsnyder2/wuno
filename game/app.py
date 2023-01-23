import data.client
import data.server
import display.gui

# display.gui.GUI()

def main():
    HOST_IP = "10.17.50.224"
    PORT = 50000

    # start server
    # sv = data.server.Server(HOST_IP, PORT)
    # sv.start()

    # start client
    c = data.client.Client(HOST_IP, PORT)
    c.connect()
    c.send("hello")


if __name__ == "__main__":
    main()

# central server should store one game instance: and multiple GUIs
