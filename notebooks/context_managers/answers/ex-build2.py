import time

class Timer():
    def __init__(self, description):
        self.description = description
        
    def __enter__(self):
        self.start = time.time()
        
    def __exit__(self, type, value, traceback):
        self.end = time.time()
        print(f"{self.description}: {self.end - self.start}")

with Timer("Timed-time:"):
    time.sleep(2)