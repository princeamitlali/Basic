li = [2,8,3,9,6,5,4]

queries = [[0,3],[1,3],[0,6]]

for i in range(1,len(li)):
    li[i] = li[i] + li[i-1]
    
for i in queries:
    if i[0] == 0:
        print(li[i[1]])
    else:
        print(li[i[1]]-li[i[0]-1])
