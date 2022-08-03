li = [8,-4,3,-5,4]
res = li[0]
for i in range(len(li)):
    curr = li[i]
    for j in range(i+1,len(li)):
        curr += li[j]
        res = max(res,curr)

print(res)