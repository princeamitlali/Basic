li = [0,1,0,2,3,0,4,0,5,0,0]
count = 0

for i in range(len(li)):
    if li[i] != 0:
        li[count] = li[i]
        li[i] = 0
        count += 1
        
print(li)