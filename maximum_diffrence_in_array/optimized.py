li = [10,8,2]
res = li[1] - li[0]
min_val = li[0]
for i in range(1,len(li)-1):
    res = max(res,li[i]- min_val)
    min_val = min(min_val,li[i])
        
print(res)