Dockerfile to run SharedArray

    docker build -t multiprocessing .
    docker run -it -v %cd%:/app multiprocessing

speed_test.py: save testing result to result.txt

SharedArray works only in OSX and Linux.

Time difference is 0.0012674331665039062
 
Time difference is 0.10327506065368652 (with SharedArray)


## References

    https://realpython.com/primer-on-python-decorators/

    https://medium.com/analytics-vidhya/multiprocessing-for-data-scientists-in-python-427b2ff93af1
