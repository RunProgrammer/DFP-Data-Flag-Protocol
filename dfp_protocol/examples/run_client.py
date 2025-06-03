from dfp import DFPClient

def main():
    client = DFPClient()
    client.connect()
    print(client.send("PING", "Hello from client"))
    #client.send("FLAG","MESSAGE")

if __name__ == "__main__":
    main()
