def repeated_strings(s, n):
    res = ""
    alist = ""
    while len(res) < n:
        res += s

    for i in res[:n]:
        if i == "a":
            alist += i
    return len(alist)


print(repeated_strings("ab", 11))
