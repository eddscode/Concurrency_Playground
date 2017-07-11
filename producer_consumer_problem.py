from threading import Thread
from queue import Queue
import random

q = Queue(maxsize=5)


class ProducerThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            if q.full() is False:
                q.put(random.randint(1, 100))


class ConsumerThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            if q.empty() is False:
                q.get()


if __name__ == '__main__':
    producer = ProducerThread()
    consumer = ConsumerThread()
    producer.start()
    consumer.start()
