def six_times_table(nums):
    for num in range(1, nums):        
        yield 6*num
        
sum(six_times_table(12))
