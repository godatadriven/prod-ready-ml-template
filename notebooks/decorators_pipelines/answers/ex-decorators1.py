def split_string(function):
    def wrapper():
        return function().split()

    return wrapper

@split_string
def say_hi():
    return 'hello, world'

say_hi()