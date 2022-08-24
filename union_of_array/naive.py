li = [1,1,2,20,40,60]

li2 = [2,20,20,20]

def union(li,li2):
    for i in li2:
        li.append(i)
    li = sorted(li)
    for i in range(len(li)):
        if i == 0 or li[i] != li[i-1]:
            print(li[i])
    
    
union(li,li2)