li = [-3,8,-2,4,-5,6]
res = li[0]
for i in li:
    res = max(res + i,i)

print(res)