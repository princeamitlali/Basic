ex = [1,5,9,4,8,3,7,3,2,1]
pivot = 3

def sort(li,pivot):
    low,mid,high = 0,0,len(li) - 1
    
    while mid <= high:
        if li[mid] < pivot:
            li[low],li[mid] = li[mid],li[low]
            mid += 1
            low += 1
        elif li[mid] == pivot:
            mid += 1
        else:
            li[mid],li[high] = li[high],li[mid]
            high -=1
    return li

print(sort(ex,pivot))