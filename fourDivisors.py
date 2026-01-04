class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # bruteforce
        # loop through nums
        # have a total 
        # if the length of the divisors of each nums is 4 
        # add it to total 
        # return total else return 0

        total = 0
        for num in nums:
            count = 0
            pretotal = 0
            for i in range(1, num + 1):
                if num % i == 0:
                    pretotal += i
                    count += 1
            if count == 4: 
                total += pretotal
        return total


        # optimized 

        total = 0
        for num in nums:
            count = 0
            pretotal = 0

            # print(sqrt(num))
            for i in range(1, int(sqrt(num)) + 1):
                if num % i == 0:
                    if i * i == num:
                        pretotal += i
                        count += 1
                    else:
                        pretotal += i + num // i
                        count += 2
            if count == 4: 
                total += pretotal
        return total
