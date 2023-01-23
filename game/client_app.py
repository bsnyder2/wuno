import data.client
import display.gui


def main():
    HOST_IP = "10.17.61.187"
    PORT = 50000

    # start client
    c = data.client.Client(HOST_IP, PORT)
    c.connect()

    c.send("hello")


if __name__ == "__main__":
    main()
