li2 = [10,4,5,8,11,6,26]
li = [1,2,3,4,5,6,7,8,9]
print(sorted(li)[4])

k = 5

def partation(arr,low,high):
    pivot_element = li[high]
    j = low - 1


    for i in range(low,high):
        if li[i] <= pivot_element:
            j += 1
            temp = li[i]
            li[i] = li[j]
            li[j] = temp 
    li[high] = li[j+1]
    li[j+1] = pivot_element
    return j + 1


def kth_element(li,k):
    low = 0
    high = len(li) -1
    while low < high:
        p = partation(li,low,high)
        if p > k  :
            high = p -1
        elif p < k:
            low = p+1
        else:
            break
            
    return li[p-1]

print(kth_element(li,k))
            