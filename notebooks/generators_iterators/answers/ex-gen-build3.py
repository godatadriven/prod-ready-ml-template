def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

fibonacci_gen = fibonacci_numbers(10)

for fibonacci_number in fibonacci_gen:
    print(fibonacci_number)