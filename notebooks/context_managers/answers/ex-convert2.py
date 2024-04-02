import contextlib        
import os
import time 

@contextlib.contextmanager
def in_dir(path):
    old_path = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(old_path)

with in_dir('../../'):
    notebook_files = os.listdir('notebooks')
    
notebook_files

@contextlib.contextmanager
def timer(description):
    start = time.time()
    yield
    end = time.time()
    print(f"{description}: {end - start}")

with timer("timed-time"):
    time.sleep(1.5)