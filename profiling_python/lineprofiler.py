# https://pypi.org/project/line_profiler/

from line_profiler import LineProfiler

def line_profile():
    def inner(func):
        def wrapper(*args, **kwargs):
            try:
                profiler = LineProfiler()
                profiler.add_function(func)
                profiler.enable_by_count()
                return func(*args, **kwargs)
            finally:
                profiler.print_stats()
        return wrapper
    return inner


@line_profile()
def expensive_function():
    for x in range(1000):
        i = x ^ x ^ x
    return 'some result!'

result = expensive_function()
