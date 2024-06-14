import datetime
import random
import socket
import threading

class Client:
    def __init__(self, nickname, host = '127.0.0.1', port = 55555):
        self.nickname = nickname
        self.id=''.join(str(random.randint(0, 9)) for _ in range(8))
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))


    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occured!")
                self.client.close()
                break

    def write(self):
        while True:
            #时间
            now = datetime.datetime.now()
            milliseconds = now.microsecond // 1000
            formatted_time_without_ms = now.strftime("%Y-%m-%d %H:%M:%S")

            formatted_time_with_ms = f"{formatted_time_without_ms}.{milliseconds:03d}"
            message = f'{formatted_time_with_ms},{self.nickname}(ID:{self.id}): {input("")}'
            self.client.send(message.encode('utf-8'))

    def run(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()