import pika
import json
import numpy as np
import time


#RABBITMQ_URL = 'amqp://guest:guest@localhost:5672//'
EXCHANGE_NAME = 'data_collection'
QUEUE_NAME1 = 'data_analysis'


max_value = float('-inf')
min_value = float('inf')

def analyze_data(device_id,data_points):
    global max_value, min_value
    if not data_points:
        return {'mean': 0, 'variance': 0, 'max': 0, 'min': 0}
    mean = np.mean(data_points)
    variance = np.var(data_points)
    max_value = max(max_value, np.max(data_points))
    min_value = min(min_value, np.min(data_points))
    print(mean,variance,min_value,max_value)
    return {'device_id': device_id, 'mean': mean, 'variance': variance, 'max': max_value, 'min': min_value}

def consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout')
    channel.queue_declare(queue=QUEUE_NAME1)
    channel.queue_bind(queue=QUEUE_NAME1, exchange=EXCHANGE_NAME, routing_key='')

    data_points_per_device = {}
    analysis_results = []

    i=0
    while True:
        i=i+1
        print(f'开始分析第{i}次')
        method, properties, body = channel.basic_get(queue=QUEUE_NAME1, auto_ack=True)
        #传输原始数据
        channel.basic_publish(exchange='', routing_key='raw_data', body=body)
        print(body)
        print(data_points_per_device)
        print(analysis_results)

        if body:
            message = json.loads(body)
            device_id = message['device_id']
            data_point = message['value']

            data_points_per_device.setdefault(device_id, []).append(data_point)

            if len(data_points_per_device[device_id]) >= 10:  # 分析每个id的10个数据点,可设置
                analysis_result = analyze_data(device_id,data_points_per_device[device_id])
                analysis_results.append(analysis_result)
                data_points_per_device[device_id] = []

                analysis_message = json.dumps(analysis_result)
                channel.basic_publish(exchange='', routing_key='analysis_results', body=analysis_message)

        time.sleep(0.35)  # 每0.35秒检查一次队列

if __name__ == '__main__':
    consumer()