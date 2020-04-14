from concurrent import futures
import time
import os

def test_process(num):
    print(str(os.getpid()).center(30,"#"))
    time.sleep(1)

data = [1,2,3,4,5,6,7,8,9,0]

if __name__ == '__main__':
    with futures.ProcessPoolExecutor(max_workers=3) as proc:
        for i in proc.map(test_process,data):
            print(111)