import functools
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {round(end - start,8)} seconds')
        return result
    return wrapper


@timer
def foo():
    a = 0
    for i in range(100000):
        a+=1
    return (a)

@timer
def foo1():
    return len(range(100000))

@timer
def foo2():
    return len(list(range(100000)))

if __name__ == '__main__':
    total_iteration = foo()
    total_iteration1 = foo1()
    total_iteration2 = foo2()
