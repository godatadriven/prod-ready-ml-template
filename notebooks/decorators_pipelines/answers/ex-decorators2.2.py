from functools import wraps 

def log_function_info(func):
    
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        print(f"The function name is {func.__name__}")
        print(f"The positional arguments are: {args}")
        print(f"The keyword arguments are: {kwargs}")
        return func(*args, **kwargs)
        
    return wrapper_function

@log_function_info
def get_factors(n):
    "Return the factors of n." 
    factors = [x for x in range(1, (n+1))
               if n % x == 0] 
    return factors

get_factors.__name__