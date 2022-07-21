li = [1,5,3,8,12]

profit = 0

for i in range(len(li)):
    if li[i-1] < li[i]:
        profit += li[i] - li[i-1]
        
print(profit)

#if increasing add to profit else ignore
