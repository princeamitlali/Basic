li = [5,4,3,2,1]

def count_and_merge(li,l,mid,r):
    left = li[:mid]
    right = li[mid:]
    n1,n2 = len(left),len(right)
    res,i,j,k = 0,0,0,l
    arr = []
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr.append(left[i])
    

def inversion(li,l,r):
    count = 0
    if l>r:
        mid = l + (r-l) //2
        count += inversion(li,l,mid)
        count += inversion(li,mid+1,r)
        count += cout_and_merge(li,l,mid,r)
    return count

print(inversion(li)) 