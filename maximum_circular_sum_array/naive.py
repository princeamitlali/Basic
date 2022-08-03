li = [5,-2,3,4]
res = li[0]
for i in range(len(li)):
    curr_sum = li[i]
    curr_max = li[i]
    for j in range(1,len(li)):
        curr_sum += li[(i+j)%len(li)]
        curr_max = max(curr_max,curr_sum)
    res = max(res,curr_max)
    
print(res)
        