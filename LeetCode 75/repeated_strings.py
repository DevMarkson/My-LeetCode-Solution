def singleNums(nums):
    for i in nums:
        # print the index of the number that is not repeated
        if nums.count(i) == 1:
            print(i)
            return i


singleNums([3, 2, 3, 4, 5])
