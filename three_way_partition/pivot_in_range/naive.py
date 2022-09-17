li = [1,0,2,9,3,8,4,7,5,6]

ran = [3,5]

def sort(li,ran):
    low,mid,high = 0,0,len(li) - 1
    
    while mid <= high:
        if li[mid] <ran[0]:
            li[low],li[mid] = li[mid],li[low]
            mid += 1
            low += 1
        elif ran[0] <= li[mid] <= ran[1]:
            mid += 1
        else:
            li[mid],li[high] = li[high],li[mid]
            high -=1
    return li

print(sort(li,ran))
        
