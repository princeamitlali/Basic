li = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]

to_find = 1

def normal_binary_search(li,to_find,start,end):
        
        while end >= start:
            mid = (end + start ) //2
            if li[mid] == to_find :
                return mid
            if li[mid] < to_find:
                start = mid + 1
            if li[mid] > to_find:
                end = mid -1
                
        return -1


def binary_search(li,to_find):
    if li[0] == to_find:
        return 0
    least = 1
    while least < len(li)-1 and li[least] < to_find:
        least *= 2
    if least > len(li)-1:
        least = len(li)- 1
    if li[least] == to_find:
        return least
    return normal_binary_search(li,to_find,least//2,least-1)
   

print(binary_search(li,to_find))
