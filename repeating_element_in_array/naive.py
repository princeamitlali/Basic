li = [0,2,1,3,2,2]
li = sorted(li)

for i in range(1,len(li)):
    if li[i] == li[i-1]:
        print(li[i])