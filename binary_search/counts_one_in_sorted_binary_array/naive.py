li = [0,0,0,1,1,1,1,1]

for i in range(len(li)):
    if li[i] == 1:
        print(len(li)-i)
        break