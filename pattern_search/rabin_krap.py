s = "geeksforggeeksforgeeks"
p = 'geek'
n = len(p)
hash_p = sum([ord(i) for i in p])
hash_s = sum([ord(s[i]) for i in range(n-1)])
arr = []
pre = 0
print(hash_p)
for i in range(n-1,len(s)):
    hash_s += ord(s[i]) - pre
    pre = ord(s[i-n])
    if hash_s == hash_p:
        if s[i-n:i] == p:
            arr.append(i-n)
print(arr)