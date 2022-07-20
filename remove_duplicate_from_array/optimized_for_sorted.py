li = [1,1,5,6,8,2,3,4,5,6,2,7]
li = sorted(li)

temp = 1

for i in li:
    if i != li[temp-1]:
        li[temp] = i
        temp += 1
    

    
print(li[:temp])
    