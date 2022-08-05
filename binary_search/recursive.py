li = [10,20,30,40,50]

to_find = 80

def binary_search(li,to_find,start,end):
    if start > end:
        return -1
    mid = (start + end) //2
    print(mid)
    if li[mid] == to_find:
        print("found")
        return mid
    elif li[mid] > to_find :
        return binary_search(li,to_find,start,mid -1)
    else:
        return binary_search(li,to_find,mid + 1, end)
    

val = binary_search(li,to_find,0,len(li)-1)
if val == -1:
    print("Not Found")
else:
    print("element is at index :::: ", val)    