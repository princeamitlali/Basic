li = [8,1,2,3,4,5,6]

flag = True
for i in range(len(li)-1):
    if li[i]>li[i+1]:
        flag = False
        break
    
print(flag)