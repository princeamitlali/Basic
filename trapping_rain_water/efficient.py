li = [5,0,6,2,3]
res = 0
lmax = [li[0]]

for i in range(1,len(li)):
    lmax.append(max(li[i],lmax[i-1]))
    
temp = li[::-1]

rmax =[temp[0]]
for i in range(1,len(li)):
    rmax.append(max(temp[i],rmax[i-1]))
    
rmax = rmax[::-1]
for i in range(len(li)):
    res += min(rmax[i],lmax[i]) - li[i]


print(res)
    