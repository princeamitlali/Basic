li = [9,4,3,8,7,6,13,13]

flag = False
for i in range(len(li)):
    flag = True
    for j in range(i,len(li)):
        if li[j] > li[i]:
            flag = False
            i = j
            break
    if flag:
        print(li[i])
        break