li1 = [2,4,6,-5,15,7]
li = [4,-4,2]

for i in range(len(li)):
    if sum(li[:i]) == sum(li[i+1:]):
        print(li[i])