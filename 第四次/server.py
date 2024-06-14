import socket
import threading

class Server:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
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
                self.broadcast(f'{nickname} left the chat!'.encode('utf-8'))
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")

            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f"Nickname of the client is {nickname}!")
            self.broadcast(f"{nickname} joined the chat!".encode('utf-8'))
            client.send('Connected to the server!'.encode('utf-8'))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    def run(self):
        print("Server started...")
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

if __name__ == '__main__':
    server = Server()
    server_thread = threading.Thread(target=server.run)
    server_thread.start()
