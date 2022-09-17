arrival = [900,600,700]
dep = [1000,800,730]

count = 1
arrival = sorted(arrival)
dep = sorted(dep)

i = 1
res =1
j = 0

while i < len(arrival) and j < len(dep) :
    if arrival[i] <= dep[j]:
        count += 1
        i += 1
    else:
        j +=1
        count -= 1
    res = max(res,count)
    print(res)
