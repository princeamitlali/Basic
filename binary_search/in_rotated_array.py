li = [10,20,30,40,50,1,3,5]

to_find = 3

def binary_search(li,to_find):
    
    start = 0
    end = len(li) -1

    while end >= start:
        mid = (end + start ) //2
        if li[mid] == to_find :
            print("found")
            return mid
        if li[start] <= li[mid]:
            if li[start] <= to_find and to_find <= li[mid]:
                end = mid -1
            else:
                start = mid + 1
        else:
            if to_find >= li[mid] and to_find <= li[end]:
                start = mid + 1
            else:
                end = mid -1

    return -1

val = binary_search(li,to_find)
print(val)   
