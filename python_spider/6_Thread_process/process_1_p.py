from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('xiaoshuaib',))
    p.start()
    p.join()