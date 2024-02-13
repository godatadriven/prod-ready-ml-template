import contextlib        
from time import time

@contextlib.contextmanager
def my_timer(description):
    start = time()
    yield 'JABBERWOCKY'
    end = time()
    print(f"{description}: {end - start}")
