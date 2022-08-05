li = [10,20,30,40,50]

to_find = 80

def binary_search(li,to_find):
    
    start = 0
    end = len(li) -1
    
    while end >= start:
        mid = (end + start ) //2
        if li[mid] == to_find :
            print("found")
            return mid
        if li[mid] < to_find:
            start = mid + 1
        if li[mid] > to_find:
            end = mid -1
            
    return -1

val = binary_search(li,to_find)
if val == -1:
    print("Not Found")
else:
    print("element is at index :::: ", val)    