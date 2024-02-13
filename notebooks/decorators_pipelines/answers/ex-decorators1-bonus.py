import time

def time_it(function):
    def wrapper():
        t1 = time.time()
        result = function()
        t2 = time.time()
        print(f'The function {function.__name__} took {round(t2-t1, 4)} seconds to run.')
        return result
    return wrapper

@time_it
def say_hi():
    return 'hello, world'

say_hi()