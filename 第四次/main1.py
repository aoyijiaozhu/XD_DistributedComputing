import client
import threading

if __name__ == '__main__':
    nickname=input('输入用户名：')
    client1 = client.Client(nickname)

    client1_thread = threading.Thread(target=client1.run)
    client1_thread.start()
