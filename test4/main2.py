import client
import threading

if __name__ == '__main__':
    nickname = input('输入用户名：')
    client2 = client.Client(nickname)

    client2_thread = threading.Thread(target=client2.run)
    client2_thread.start()