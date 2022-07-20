li = [1,2,3,4,5,6]

flag = True
init = li[0]
for i in li:
    if i < init:
        flag = False
        break
    init = i
                  
print(flag)
    