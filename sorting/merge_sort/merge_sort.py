

def merge(arr,low,mid,high):
    li = arr[low:mid]
    li2 = arr[mid:high]   
    m,n = len(li),len(li2)
    i,j = 0,0
    arr = []
    while i < m and j < n :
        if li[i] <= li2[j]:
            arr.append(li[i])
            i += 1
        else:
            arr.append(li2[j])
            j += 1
    while i<m:
        arr.append(li[i])
        i += 1
    while j < n:
        arr.append(li2[j])
        j += 1
    


def merge_sort(arr,l,r):
    if r > l:
        mid = l + (r-l)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge(arr,l,mid,r)
    return arr
arr = [1,2,4,7,3,5,9,8,5]

print(merge_sort(arr,0,9))
print(arr)