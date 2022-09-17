li = [1,2,3,4,5,6,7,8,9]

temp = []

for i in li:
    if i %2 == 0:
        temp.append(i)
        li.pop(li.index(i))
        
for i in li:
    temp.append(i)
    
print(temp)