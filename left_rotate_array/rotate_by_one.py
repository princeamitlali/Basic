li = [1,2,3,4,5]

temp = li[0]

for i in range(1,len(li)):
    li[i-1] = li[i]
    
li[len(li)- 1] = temp

print(li)