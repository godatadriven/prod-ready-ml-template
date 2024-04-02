import os 

class InDir:
    def __init__(self, path):
        self.old_path = os.getcwd()
        self.path = path

    def __enter__(self):
        os.chdir(self.path)
        return None

    def __exit__(self, exc_class, exc, traceback):
        os.chdir(self.old_path)

with InDir('../../'):
    notebook_files = os.listdir('notebooks')
    
notebook_files