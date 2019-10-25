import time

def test_speed(func):
    def speed(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        # print('Time difference is {}'.format(end-start))
        with open('result.txt', 'a') as file:
            file.write('Time difference is {}\n'.format(end-start))
    return speed
