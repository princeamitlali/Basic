li = [1,2,20,40,60]

li2 = [2,20,20,20]

def intersection(li,li2):
    m,n = len(li),len(li2)
    
    for i in range(m):
        if i>0 and li[i] == li[i-1]:
            continue
        for j in range(n):
            if li[i] == li2[j]:
                print(li[i])
                break
            
            
intersection(li,li2)