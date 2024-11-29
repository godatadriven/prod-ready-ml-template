
from functools import wraps

# To define arguments, you wrap the actual decorator function around another function defining the arguments.
def change_case(upper = True):
    
    def decorator_function(func):
 
        @wraps(func)
        def wrapper(*args, **kwargs):
            if upper:
                return func(*args, **kwargs).upper()
            else:
                return func(*args, **kwargs).lower()
           
        return wrapper
    
    return decorator_function

@change_case(upper = True)
def say_hi(name):
    return f"Hello {name}!"

say_hi("people")