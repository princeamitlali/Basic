li = [0,2,1,3,2,2]


for i in range(len(li)):
    if li[i] in li[i+1:]:
        print(li[i])