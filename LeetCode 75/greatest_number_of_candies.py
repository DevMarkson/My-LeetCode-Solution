class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        # Get the total number of kids
        n = len(candies)

        # Initialize a boolean array with all elements set to False
        result = [False] * n

        # Find the maximum number of candies among all the kids
        maximum_candies = max(candies)

        # Iterate through each kid's candies
        for i in range(n):
            # Check if the sum of the kid's candies and the extra candies is greater than or equal to the maximum number of candies
            if candies[i] + extraCandies >= maximum_candies:
                # If the condition is true, set the corresponding index in the result array to True
                result[i] = True

        # Return the result array
        return result

# Example test case
candies = [2, 3, 5, 1, 3]
extraCandies = 3
solution = Solution()
print(solution.kidsWithCandies(candies, extraCandies))
