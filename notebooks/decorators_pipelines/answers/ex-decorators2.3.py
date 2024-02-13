
def time_it(function):
    import time
    
    def wrapper(*args):
        t1 = time.time()
        result = function(*args)
        t2 = time.time()
        print(f'The function {function.__name__} took {round(t2-t1, 4)} seconds to run.')
        return result

    return wrapper

def is_prime(function):
    
    def wrapper(*args):
        result = function(*args)
        if len(result) == 2:
            print(f"{args[0]} is a prime number.")
        else:
            print(f"{args[0]} is not a prime number.")
        return result
    return wrapper

@is_prime
@time_it
def get_factors(n):
    "Return the factors of n." 
    factors = [x for x in range(1, (n+1))
               if n % x == 0] 
    return factors

get_factors(1254739)