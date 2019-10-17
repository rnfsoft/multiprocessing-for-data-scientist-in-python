import time

def test_speed(func):
    def speed(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Time difference is {}'.format(end-start))
    return speed
