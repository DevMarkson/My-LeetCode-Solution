def twoSum(nums, target):
    # create an empty hashmap to store the numbers and their indexes
    previousMap = {}

    # since we need the index and the actual number in the array we use enumerate
    for index, num in enumerate(nums):
        # we find the difference between the target and the number
        diff = target - num
        # we check if the difference is already in our hash map
        if diff in previousMap:
            return [previousMap[diff], index]
        previousMap[num] = index
    

print(twoSum([1, 2, 3, 5, 4], 4))
