from math import factorial


def lexiograpic_rank(s):
    n = len(s)
    res = 0
    for i in range(n):
        v = 0
        for j in range(i+1,n):
            if s[j] < s[i]:
                v += 1
        val = v
        res += (val) * factorial(n-i-1)
        print(val,n-i-1)
    return res + 1

print(lexiograpic_rank("string"))