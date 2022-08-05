li = [10,12]

def peek_element(li):
    n = len(li)
    start = 0
    end = n -1
    while end >= start:
        mid = (start + end) // 2
        if (mid == 0 or li[mid -1] <= li[mid] ) and (mid == n-1 or li[mid + 1] <= li[mid]):
            return mid
        if mid > 0 and li[mid -1 ] >= li[mid]:
            end = mid -1
        else:
            start = mid +1
            
print(li[peek_element(li)])