li = [0,1,0,2,3,0,4,0,5,0,0]


for i in range(len(li)):
    if li[i] == 0:
        li.pop(i)
        li.append(0)
        
print(li)