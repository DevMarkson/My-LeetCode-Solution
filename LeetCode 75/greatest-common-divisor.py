class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        # Check if either str1 or str2 is empty, return an empty string
        if not str1 or not str2:
            return ""
        
        # Check if str1 is equal to str2, return str1 or str2
        if str1 == str2:
            return str1

        # Swap str1 and str2 if str1 is longer
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        # Loop until str1 is empty
        while str1:
            # Check if str1 doesn't start with str2
            if not str2.startswith(str1):
                return ""
            
            # Remove the portion of str2 that is equal to str1
            str2 = str2[len(str1):]
            
            # Swap str1 and str2 if str1 is longer than str2
            if len(str1) > len(str2):
                str1, str2 = str2, str1
        
        # Return the largest common divisor (GCD) stored in str2
        return str2
