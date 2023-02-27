s = "geeks for ggeeks for geeks"
p = 'geek'
n = len(p)
arr = []
i = 0
while i < len(s):
    try:
        if s[i:i+ n] == p:
            v = i

            arr.append(v)
            i += n
        else:
            i += 1
    except:
        break
print(arr)