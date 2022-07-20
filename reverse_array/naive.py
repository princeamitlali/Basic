li = [1,2,3,4,5,6]

temp_li = []

for i in li:
    temp_li.append(i)
    
j = 0
for i in range(len(temp_li) -1,-1,-1):
    li[j] = temp_li[i]
    j += 1
    
print(li)
    