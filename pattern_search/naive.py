s = "aaaaaa"
p = 'aa'
n = len(p)
arr = []
for i in range(len(s)-n+1):
    if s[i:i+n] == p:
        arr.append(i)
print(arr)