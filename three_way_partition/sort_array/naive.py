li = [1,0,2,2,1,1,0,0,0,0,1]

def sort(li):
    low,mid,high = 0,0,len(li) - 1
    
    while mid <= high:
        if li[mid] == 0:
            li[low],li[mid] = li[mid],li[low]
            mid += 1
            low += 1
        elif li[mid] == 1:
            mid += 1
        else:
            li[mid],li[high] = li[high],li[mid]
            high -=1
    return li

print(sort(li))
        
