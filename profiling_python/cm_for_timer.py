# context manager for timer
import time

def foo():
    a = 0
    for i in range(100000):
        a+=1
    return (a)

def foo1():
    return len(range(100000))

def foo2():
    return len(list(range(100000)))

class timer():
    def __init__(self, name=''):
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def checkpoint(self, name = ''):
        print(f'{name} took {self.elapsed} seconds')

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.checkpoint('finished')

if __name__ = '__main__':
    with timer() as timer:
        foo()
        timer.checkpoint('foo')
        foo1()
        timer.checkpoint('foo1')
        foo2()
        timer.checkpoint('foo2')
