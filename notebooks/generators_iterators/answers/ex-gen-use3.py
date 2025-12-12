from functools import reduce
import operator

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

reduce(operator.mul, fibonacci_numbers(10))