import socket
import threading


class InterplanetaryCommunicationProtocol:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(5)
        self.clients = []
        self.nicknames = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(f"{nickname} left the chat!".encode("utf-8"))
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")

            client.send("NICK".encode("utf-8"))
            nickname = client.recv(1024).decode("utf-8")
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f"Nickname of client is {nickname}!")
            self.broadcast(f"{nickname} joined the chat!".encode("utf-8"))
            client.send("Connected to the server!".encode("utf-8"))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    def implementCommunicationProtocol(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()


if __name__ == "__main__":
    protocol = InterplanetaryCommunicationProtocol("127.0.0.1", 55555)
    protocol.implementCommunicationProtocol()
