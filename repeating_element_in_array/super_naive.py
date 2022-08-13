li = [0,2,1,3,2,2]

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] == li[j]:
            print(li[i],li[j])
        