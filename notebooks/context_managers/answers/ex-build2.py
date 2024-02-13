import sys
import contextlib        

@contextlib.contextmanager
def looking_glass():
    
    # preserve the original functionality
    original_write = sys.stdout.write
    
    # define custom function to reverse print statements
    def reverse_write(text):
        original_write(text[::-1])
    
    # replace with the new function
    sys.stdout.write = reverse_write
    
    yield 'JABBERWOCKY'
        
    # tear down context and revert to original print functionality
    sys.stdout.write = original_write