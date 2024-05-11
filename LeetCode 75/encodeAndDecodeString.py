def encode(strs):
    res = ""
    for s in strs:
        res += str(len((s))) + "#" + s
    return res 

def decode(str):
    res = []
    i = 0

    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j + 1: j + 1 + length])
        i = j + 1 + length
    return res




res_encode = encode(["hello","Mark", "boy"])
res_decode = decode(res_encode);
print(res_encode)
print(res_decode)

