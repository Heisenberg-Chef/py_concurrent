from concurrent import futures

def test(num):
    import time
    time.sleep(1)
    return time.asctime(),num

data = [1,2,3]
with futures.ThreadPoolExecutor(max_workers=3) as Exec:
    for future in Exec.map(test,data):
        print(future)