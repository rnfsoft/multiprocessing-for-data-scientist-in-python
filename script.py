import numpy as np
import math
import time
from speed_test import test_speed
fake_data = np.random.random((100, 10000000)) # row, column: random((3, 2)) eg. [[0.72202131 0.56485077] [0.07333937 0.89956364] [0.10147896 0.30743569]]

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