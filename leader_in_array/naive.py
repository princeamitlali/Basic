li = [7,10,4,10,6,5,2]

for i in range(len(li)):
    flag = True
    for j in range(i+1,len(li)):
        if li[j] >= li[i]:
            flag = False
            break
    if flag:
        print(li[i])