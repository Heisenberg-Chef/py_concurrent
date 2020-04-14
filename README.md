#   python concurrent库
+   python因为其全局解释器锁GIL而无法实现真正的平行运算，concurrent.futures模块是对于multiprocessing的再封装：使用子进程的形式平行运行python解释器利用多CPU来提高执行速度，由于子进程和主解释器分离，所以他们得全局解释器锁也是相对独立的。每个子进程都能完成的使用一个CPU内核。3.2以后的PYTHON内核已经集成了concurrent.futures模块
+   Executor对象：是一个抽象类，它提供了一步调用的方法，它不能直接使用，但是可以通过他的2个子类ThreadPoolExecutor或者ProcessPoolExecutor进行调用。
    +   submit(fn,*args,**kwargs)来提交运行函数和变量，submit函数返回一个future对象，future提供了耿总任务状态的方法，比如判断任务是否完成future.done()。
    +   map(func,*iterable,timeout) 带有迭代器的传参函数。
    +   shutdown：释放系统资源。可以使用with语法来避免显式调用法。
