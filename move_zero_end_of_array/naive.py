li = [0,1,0,2,3,0,4,0,5,0,0]

for i in range(len(li)):
    if li[i] == 0:
        for j in range(i+1,len(li)):
            if li[j] != 0:
                li[i] = li[j]
                li[j] = 0
                break

print(li)