li = [2,20,20,40,60]
li2 = [2,10,20,20]

def union(li,li2):
    m,n = len(li),len(li2)
    i,j = 0,0
    while i<m and j < n:
        if i >0 and li[i] == li[i-1]:
            i += 1
            continue
        if j > 0 and li2[j] == li2[j-1]:
            j += 1  
            continue
        if li[i]< li2[j]:
            print(li[i])
            i += 1
        elif li[i] > li2[j]:
            print(li2[j])
            j += 1
        else:
            print(li[i])
            i += 1
            j += 1
    while i < m:
        print(li[i])
        i += 1
    while j < n :
        print(li2[j])
        j += 1
    
union(li,li2)