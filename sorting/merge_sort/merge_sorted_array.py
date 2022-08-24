def merge(li,li2):
    temp = []
    i,j = 0,0
    m,n = len(li),len(li2)
    while i < m and j < n :
        if li[i] <= li2[j]:
            temp.append(li[i])
            i += 1
        else:
            temp.append(li2[j])
            j += 1
    while i<m:
        temp.append(li[i])
        i += 1
    while j < n:
        temp.append(li2[j])
        j += 1
    return temp