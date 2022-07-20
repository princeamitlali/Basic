li = [1,2,3,4,5,6,5,4,3,9,11,2]

flag = False
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[j] < li[i]:
            flag = True
            break
    if flag:
        break
                  
print(not flag)
    