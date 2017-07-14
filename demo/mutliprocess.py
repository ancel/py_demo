
def hello(name):
    print('hello {}!'.format(name))

persons = []
persons.append('aaa')
persons.append('ccc')
persons.append('ddd')

print('hello')

def multi_thread():
    # 多线程
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool(2)
    pool.map(hello, persons)
    pool.close()
    pool.join()

def multi_process():
    # 多进程
    import multiprocessing
    for name in persons:
        p = multiprocessing.Process(target=hello, args=(name,))
        p.start()


if __name__ == '__main__':
    print('main')
    multi_thread()
    multi_process()
    


    
