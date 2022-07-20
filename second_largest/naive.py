li = [9,9,9]


#first get the largest
flag = False
largest = 0
for i in range(len(li)):
    flag = True
    for j in range(i,len(li)):
        if li[j] > li[i]:
            flag = False
            i = j
            break
    if flag:
        largest = li[i]
        break
    
#compute second largest
second_largest = -1
for i in li:
    if i == largest:
        continue
    if i > second_largest:
        second_largest = i
        
print(second_largest)
    
