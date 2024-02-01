def validAnagram(s, t):
    # if they are of the same length definitely they are not anagrams of each other
    # hence return false
    if len(s) != len(t):
        return False
    
    # create a hash map for S and T 
    countS = {}
    countT = {}

    # iterate through the length of the string and assign a key-value pair to each characters by their occurence
    for i in range(len(s)):
        #anytime we see the character we want to increment the count by 1 and use get to get the key and 0 is the default if the key doesn't exist
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

        # print(countS[s[i]])
        # print(countS)
        # print(countT[t[i]])
        # print(countT)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

s = "anagram"
t = "nagaram"  
print(validAnagram(s, t))