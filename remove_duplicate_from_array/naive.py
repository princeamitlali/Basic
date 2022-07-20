li = [1,1,5,6,8,2,3,4,5,6,2,7]

temp_li = []

for i in li:
    temp_li.append(i)
    
li = []
for i in temp_li:
    if i not in li:
        li.append(i)
    
print(li)
    