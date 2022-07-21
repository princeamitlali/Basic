li = [2,3,10,6,4,8,1]
res = 0

for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        res = min(res,li[j] - li[i])
        
print(res)