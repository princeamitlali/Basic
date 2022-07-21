li = [1,2,3,4,5,6]

res = 1
for i in range(len(li)):
    curr = 1
    for j in range(i+1,len(li)):
        if (li[j-1] + li[j]) %2 == 1:
            curr += 1
        else:
            break
    res = max(res,curr)
   
res = max(res,curr) 
print(res)