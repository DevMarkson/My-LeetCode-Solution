def duplicate(nums):
    unique_set = set()
    for num in nums:
        if num in unique_set:
            return True
        else:
            unique_set.add(num)
    return False

nums = [2, 4, 5, 6, 3]
print(duplicate(nums))