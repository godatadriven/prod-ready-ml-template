def six_times_table(nums):
    for num in range(1, nums):        
        yield 6*num

num_gen = six_times_table(10)

for num in num_gen:
    print(num)