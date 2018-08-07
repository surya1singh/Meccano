import cProfile


def profiler(func):
    def wrapper(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return wrapper





def foo():
    a = 1
    for i in range(100000):
        a*=foo1()

def foo1():
    return len(range(100000))

@profiler
def foo2():
    foo()
    return len(list(range(100000)))

if __name__ == '__main__':
    total_iteration = foo2()
