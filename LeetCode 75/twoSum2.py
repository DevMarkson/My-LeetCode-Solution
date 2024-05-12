def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        currentSum = numbers[l] + numbers[r]
        if currentSum > target:
            r -= 1
        elif currentSum < target:
            l += 1
        else: 
            return [l + 1, r + 1]

    
print(twoSum([1,3,4,5,7,11], 8))
    