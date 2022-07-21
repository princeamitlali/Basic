li = [5,0,6,2,3]
res = 0
for i in range(1,len(li)-1):
    lmax = max(li[i],max(li[:i]))
    rmax = max(li[i],max(li[i+1:]))
    res += min(lmax,rmax) - li[i]
    
print(res)
    