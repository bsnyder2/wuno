import data.server


def main():
    HOST_IP = "10.17.50.224"
    PORT = 50000

    # start server
    sv = data.server.Server(HOST_IP, PORT)
    sv.start()


if __name__ == "__main__":
    main()
