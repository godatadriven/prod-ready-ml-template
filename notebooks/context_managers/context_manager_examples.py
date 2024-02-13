from time import time


class Timer(object):
    def __init__(self, description):
        self.description = description
    def __enter__(self):
        self.start = time()
    def __exit__(self, type, value, traceback):
        self.end = time()
        print(f"{self.description}: {self.end - self.start}")


import contextlib        

@contextlib.contextmanager
def my_timer(description):
    from time import time
    start = time()
    yield
    end = time()
    print(f"{description}: {end - start}")


class LookingGlass:
    
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
    
    def reverse_write(self, text):
        self.original_write(text[::-1])
        
    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write


import sys


@contextlib.contextmanager
def looking_glass():
        
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
        
    sys.stdout.write = reverse_write
    
    yield 'JABBERWOCKY'
    
    sys.stdout.write = original_write

