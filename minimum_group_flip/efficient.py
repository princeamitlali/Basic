li = [0,0,1,1,0,0,1,1,1,1]
flag = True
for i in range(1,len(li)-1):
    if li[i] != li[i-1]:
        if flag:
            print("start fliping at :: ", i)
            flag = False
        else:
            print("End fliping at :: ", i-1)
            flag = True
            
if not flag:
    print("End fliping at :: ", len(li)- 1)