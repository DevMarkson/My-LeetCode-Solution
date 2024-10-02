def plus_minus(n, nums):
    plus_count = 0
    neg_count = 0
    zero_count = 0
    for i in range(n):
        if nums[i] > 0:
            plus_count += 1
        elif nums[i] < 0:
            neg_count += 1
        else:
            zero_count += 1
    print(plus_count/n)
    print(neg_count/n)
    return zero_count/n


print(plus_minus(6, [-4, 3, -9, 0, 4, 1]))
