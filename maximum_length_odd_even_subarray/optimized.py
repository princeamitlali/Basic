li = [1,1,2,3,4,5,6]

res=1
curr = 1
for i in range(len(li)):
    if (li[i-1] + li[i ]) %2 == 1:
        curr += 1
        res = max(curr,res)

    else:
        curr = 1
   
print(res)