import multiprocessing
import pika
import json
import numpy as np
import time

# RabbitMQ连接配置
#RABBITMQ_URL = 'amqp://guest:guest@localhost:5672//'
EXCHANGE_NAME = 'data_collection'

def producer(device_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout')

    while True:

        data_point = np.random.normal()
        timestamp = time.time()

        message = {
            'device_id': device_id,
            'timestamp': timestamp,
            'value': data_point
        }

        channel.basic_publish(exchange=EXCHANGE_NAME, routing_key='', body=json.dumps(message))
        print('id:'+str(device_id),json.dumps(message))

        time.sleep(1)

if __name__ == '__main__':

    processes = []
    for i in range(3):  # 假设有3个设备
        process = multiprocessing.Process(target=producer, args=(i,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()