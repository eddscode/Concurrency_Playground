import numpy as np
from threading import Thread


class MapReduce(Thread):
    def __init__(self, text_file, thread = 1):
        Thread.__init__(self)
        self.text_file = text_file
        self.thread_count = thread

    @staticmethod
    def read_data(text_file):
        bag_of_words = open(text_file).read().split()
        return bag_of_words

    @staticmethod
    def split_data_into_subarrays(bag_of_words, thread_count):

        total_words = len(bag_of_words)
        arr = []
        i = 0
        section_length = total_words / thread_count

        while i < thread_count - 1:
            arr.insert([bag_of_words[i * section_length:(i + 1) * section_length]])
            i += 1

        return arr

    """
    def map(self, text_file):

        arr = []
        words = open(text_file).read().split()
        for word in words:
            arr.insert(0, word)

        return arr
    """

    def reduce(self, arr):
        arr_unique = np.unique(arr)
        output = {}
        for word in arr_unique:
            count = arr.count(word)
            output[word] = count

        return output

    def run(self):
        bag_of_words = MapReduce.read_data(self.text_file)
        arr = MapReduce.split_data_into_subarrays(bag_of_words, self.thread_count)
        return MapReduce.reduce(self, arr)


if __name__ == '__main__':
    mr = MapReduce('test.txt')
    print(mr.run())
