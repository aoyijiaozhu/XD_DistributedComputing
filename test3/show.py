import pika
import json
import matplotlib.pyplot as plt


QUEUE_NAME = 'analysis_results'
QUEUE_NAME2 = 'raw_data'


raw_data_points_per_device = {}
data_points_per_device = {}

def shower():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)
    channel.queue_declare(queue=QUEUE_NAME2)

    plt.ion()
    fig, axs = plt.subplots(2)

    while True:
        #原始数据
        method2, properties2, body2 = channel.basic_get(queue=QUEUE_NAME2, auto_ack=True)
        print(body2)
        if body2:
            raw_data = json.loads(body2)

            device_id = raw_data['device_id']
            value = raw_data['value']

            raw_data_points_per_device.setdefault(device_id, []).append(value)
            if len(raw_data_points_per_device[device_id]) > 100:  # 如果数据点超过100个，删除最旧的数据点
                raw_data_points_per_device[device_id].pop(0)


            axs[0].clear()
            for device_id, data_points in raw_data_points_per_device.items():
                axs[0].plot(data_points, label=f"Device {device_id}")
            axs[0].set_title("Device Raw_Data")
            axs[0].legend(loc='upper left')

        #分析之后的数据
        method, properties, body = channel.basic_get(queue=QUEUE_NAME, auto_ack=True)
        print(body)
        if body:
            analysis_result = json.loads(body)

            device_id = analysis_result['device_id']
            mean = analysis_result['mean']
            variance = analysis_result['variance']
            max = analysis_result['max']
            min = analysis_result['min']
            print(device_id, mean, variance, max, min)

            data_points_per_device.setdefault(device_id, []).append(mean)
            if len(data_points_per_device[device_id]) > 100:  # 如果数据点超过100个，删除最旧的数据点
                data_points_per_device[device_id].pop(0)


            axs[1].clear()
            for device_id, data_points in data_points_per_device.items():
                axs[1].plot(data_points, label=f"Device {device_id}")
            axs[1].set_title("Device Data Analysis")
            axs[1].legend(loc='upper left')

        plt.draw()
        plt.pause(0.01)


if __name__ == '__main__':
    shower()
