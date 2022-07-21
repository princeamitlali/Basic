li = [1,-2,3,-1,2]
res = li[0]
for i in range(len(li)):
    curr = 0
    for j in range(i+1,len(li)):
        curr += li[j]
        res = max(res,curr)

print(res)