li = [1,0,0,1,1,0,1,0,1]

temp = []
j = 0

for i in li:
    if i == 0 :
        temp.append(i)
    else:
        temp.insert(j,1)
        j += 1
        
    
print(temp)