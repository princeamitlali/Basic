li = [20,5,40,60,10,30]

for i in range(1,len(li)):
    key = li[i]
    j = i-1
    while(j>=0 and li[j] > key):
        li[j+1] = li[j]
        j -= 1
    li[j+1] = key
    print(li)