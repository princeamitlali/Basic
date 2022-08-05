li = [10,20,30,40,50,80,80,80]

to_find = 80

def first_occurance(li,to_find):
    
    start = 0
    end = len(li) -1
    
    while end >= start:
        mid = (end + start ) //2
        if li[mid] < to_find:
            start = mid + 1
        elif li[mid] > to_find:
            end = mid -1
        else:
            if mid == 0 or li[mid-1] != li[mid]:
                return mid
            else:
                end = mid -1
            
    return -1

val = first_occurance(li,to_find)
if val == -1:
    print("Not Found")
else:
    print("element is at index :::: ", val)    