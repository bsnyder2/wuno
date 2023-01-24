import data.client


def main():
    HOST_IP = "10.17.50.224"
    PORT = 50000

    # start client
    c = data.client.Client(HOST_IP, PORT)
    c.connect()


if __name__ == "__main__":
    main()
