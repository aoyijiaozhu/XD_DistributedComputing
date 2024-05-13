#初始化所有队列
import pika

QUEUE_NAME = 'analysis_results'
QUEUE_NAME2 = 'raw_data'
QUEUE_NAME3 = 'data_analysis'

def clear_queues():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_purge(queue=QUEUE_NAME)
    channel.queue_purge(queue=QUEUE_NAME2)
    channel.queue_purge(queue=QUEUE_NAME3)
    print('OK')

if __name__ == '__main__':
    clear_queues()
