def isPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
word = "madams"
print(isPalindrome(word))