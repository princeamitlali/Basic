li = [[5,10],[2,3],[6,8],[1,7]]

li = sorted(li, key = lambda x : x[0])

print(li)
mi = li[0][0]
mx = li[0][1]
for i in range(len(li)-1):
    if mx < li[i+1][0]:
        print(mi,mx)
        mi = li[i+1][0]
        mx = li[i+1][1]
    else:
        if mx < li[i+1][1]:
            mx = li[i+1][1]
    # print(mi,mx)
        
print(mi,mx)