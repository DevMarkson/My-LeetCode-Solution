def productExceptSelf(nums):
    output = []
    total = 1
    for i in nums:
        total *= i

    for i in nums:
        num = total / i
        print(num)

nums = [1,2,3,4]
print(productExceptSelf(nums));
