li = [0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,]
res = 0

for i in range(len(li)):
    curr = 0
    for j in range(i,len(li)):
        if li[j] == 1:
            curr += 1
        else:
            break
    res = max(res,curr)
    # print(curr)
    
print(res)