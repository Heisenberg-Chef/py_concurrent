from concurrent import futures
 
def test(num):
    import time
    return time.ctime(),num
 
with futures.ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(test,1)
    print(future.result())