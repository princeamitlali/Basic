def naive(s1,s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2
print(naive("listen",'silient'))