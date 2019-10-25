import numpy as np
import math
import time
from speed_test import test_speed
x_dim, y_dim = 100, 1000
fake_data = np.random.random((x_dim, y_dim)) # row, column: random((3, 2)) eg. [[0.72202131 0.56485077] [0.07333937 0.89956364] [0.10147896 0.30743569]]

@test_speed
def process_data(fake_data):
    data = fake_data.copy()

    for i, row in enumerate(data):
        for j, data_point in enumerate(row):
            if data_point == None:
                data[i,j] = 0
            data[i,j] = math.exp(math.sqrt(data_point))
        return data
process_data(fake_data)


import SharedArray
import multiprocessing
@test_speed
def multiprocess_data(fake_data):
    data = SharedArray.create('data', (x_dim, y_dim))
    
    def calc_row(i):
        for j, data_point in enumerate(fake_data[i]):
            if data_point == None:
                data[i, j] = 0
            data[i, j] = math.exp(math.sqrt(data_point))
    
    processes = []
    for i in range(len(fake_data)):
        process = multiprocessing.Process(target=calc_row, args=(i,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    return data
multiprocess_data(fake_data)
SharedArray.delete('data')