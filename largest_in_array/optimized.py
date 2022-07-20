li = [5,4,3,2,1,2,3,4,5,6]

flag = li[0]
for i in li:
    if i > flag:
        flag = i
print(flag)
    