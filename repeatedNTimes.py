class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # first solution
        # nums length = 2 * n
        # 4 = 2 * n
        # n = 2
        # divide len of nums by 2 
        # loop through to see which element has that same amount
        # can use dictionary to store the values


        numDict = {}

        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1

        n = len(nums) // 2
        for key, values in numDict.items():
            if values == n:
                return key

            
        # second solution
        # because other element occur at least once
        # using a set to solve it works

        numSet = set()
        for num in nums:
            if num in numSet:
                return num
            numSet.add(num)
            
