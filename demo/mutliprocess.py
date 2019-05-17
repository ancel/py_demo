
def hello(name):
    print('hello {}!'.format(name))


# 斐波那契数列
def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)

# 多线程
def multi_thread():
    from multiprocessing.dummy import Pool
    pool = Pool(3)
    pool.map(hello, persons)
    pool.close()
    pool.join()

# 线程池
def multi_thread_pool():
    from concurrent.futures import ThreadPoolExecutor, as_completed
    nums = range(1, 10)
    with ThreadPoolExecutor(max_workers=3) as executor:
        for num, result in zip(nums, executor.map(fib, nums)):
            print('fib({}) = {}'.format(num, result))

def multi_thread_pool_2():
    from concurrent.futures import ThreadPoolExecutor, as_completed
    nums = range(1, 10)
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_to_num = {executor.submit(fib, num): num for num in nums}
        for future in as_completed(future_to_num):
            num = future_to_num[future]
            try:
                result = future.result()
            except Exception as e:
                print('raise an exception: {}'.format(e))
            else:
                print('fib({}) = {}'.format(num, result))


# 多进程
def multi_process():
    import time
    from multiprocessing.pool import Pool
    nums = range(1, 10)
    start = time.time()
    pool = Pool(3)
    for num, result in zip(nums, pool.map(fib, nums)):
        print('fib({}) = {}'.format(num, result))
    print('COST: {}'.format(time.time() - start))

# 进程池
def multi_process_pool():
    import time
    from concurrent.futures import ProcessPoolExecutor, as_completed
    nums = range(25, 38)
    
    start = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        for num, result in zip(nums, executor.map(fib, nums)):
            print('fib({}) = {}'.format(num, result))
    print('COST: {}'.format(time.time() - start))

# 进程池2
def multi_process_pool():
    import time
    from concurrent.futures import ProcessPoolExecutor, as_completed
    nums = range(25, 38)
    
    start = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(fib, num): num for num in nums}
        for f in as_completed(futures):
            try:
                LOGGER.info('%s result is %s', futures[f], f.result())
            except Exception as e:
                LOGGER.error('%s result False' % futures[f], e)
    print('COST: {}'.format(time.time() - start))



def sync():
    import multiprocessing
    manager = multiprocessing.Manager()
    dt = manager.dict()
    lt = manager.list()
    sema = manager.Semaphore(3)

    r_lock = manager.RLock()
    r_lock.acquire()  #申请锁
    print('I am locked')
    r_lock.release()   #释放锁
    print('I am freedom')

    lock = manager.Lock()
    lock.acquire()  #申请锁
    print('I am locked')
    lock.release()   #释放锁
    print('I am freedom')

# sum=0

sum = 0
def add(n):
    global sum
    sum = sum+n

def sync_process():
    import time
    from concurrent.futures import ProcessPoolExecutor, as_completed
    import multiprocessing
    manager = multiprocessing.Manager()
    sum = manager.Value('i',0)
    nums = []
    for i in range(100): 
        nums.append(1)
    start = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        executor.map(add, nums)
    print(sum.value)
    print('COST: {}'.format(time.time() - start))

def f(x, arr, l):
    x.value = 3.14
    arr[0] = 5
    l.append('Hello')

def sync_process_2():
    import multiprocessing

    # 1、在主进程的内存空间中创建共享的内存
    # num   = multiprocessing.Value('d', 0.0)

    # 2、Manager对象类似于服务器与客户之间的通信 (server-client)，与我们在Internet上的活动很类似。
    # 我们用一个进程作为服务器，建立Manager来真正存放资源。其它的进程可以通过参数传递或者根据地址来访问Manager，
    # 建立连接后，操作服务器上的资源
    # 嵌套共享数据也必须使用mananger生成

    # Data can be stored in a shared memory map using Value or Array. 
    # 只有Value和Array可以共享，且必须作为参数传入进程
    server = multiprocessing.Manager()
    x    = server.Value('d', 0.0)
    arr  = server.Array('i', range(10))
    l    = server.list()

    proc = multiprocessing.Process(target=f, args=(x, arr, l))
    proc.start()
    proc.join()

    print(x.value)
    print(arr)
    print(l)

def sync_thread():
    import time
    from concurrent.futures import ThreadPoolExecutor, as_completed
    nums = []
    for i in range(1000): 
        nums.append(1)
    
    start = time.time()
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(add, nums)
    print(sum)
    print('COST: {}'.format(time.time() - start))



def add_item(s):
    pv_dif_dict[s] = 1
if __name__ == '__main__':
    # multi_thread()
    # multi_process()
    # multi_process_pool()
    # multi_thread_pool()
    # multi_thread_pool_2()
    # sync()
    sync_process_2()
    # sync_process()
    # sync_thread()
    from concurrent.futures import ProcessPoolExecutor, as_completed
    import multiprocessing
    manager = multiprocessing.Manager()
    pv_dif_dict = manager.dict()
    ss = []
    ss.append('123')
    ss.append('345')
    ss.append('678')
    with ProcessPoolExecutor(max_workers=8) as executor:
        executor.map(add_item, ss)
    print(pv_dif_dict)

    


    
