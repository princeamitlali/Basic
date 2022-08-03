li = [0,0,1,1,0,0,1,1,1,1]
val = li[0]
flag = True
count = 0
for i in range(len(li)):
    if li[i] != val:
        if flag:
            print("start flip :: ",i)
            count += 1
            flag = False 
    else:
        if not flag:
            print("end flip :: ",i-1)
        flag = True

if not flag:
    print("end flip :: ",i)
                 
print(count)