from functools import wraps


def change_case(upper):
    
    def decorator(function):
        
        def wrapper(*args, **kwargs):
            if upper:
                return function(*args, **kwargs).upper()
            return function(*args, **kwargs)

        return wrapper
        
    return decorator

@change_case(upper=True)
def say_hi(who):
    return f"Hello {who}!"

say_hi("people")