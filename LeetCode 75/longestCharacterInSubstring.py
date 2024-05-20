def longestCharacterInSubstring(s):
    l = 0
    characterSet = set()
    res = 0

    for r in range(len(s)):
        while s[r] in characterSet:
            characterSet.remove(s[l])
            l += 1
        characterSet.add(s[r])
        res = max(res, r - l + 1 )
    return res

s = "abcabcbb"
print(longestCharacterInSubstring(s))
