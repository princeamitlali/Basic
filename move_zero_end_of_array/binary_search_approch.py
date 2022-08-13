li = [10,2,20]
s = 2


def is_feasible(li,n,s,mid):
    req ,summ = 1,0
    for i in range(n):
        if summ + li[i] > mid:
            req += 1
        else:
            summ += li[i]
    return req <= s
    

def min_page_allocated(li,s):
    mx = max(li)
    summ = sum(li)
    low = mx
    high = summ
    res = 0
    
    while low <= high:
        mid = (low + high) //2
        
        if is_feasible(li,len(li),s,mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

print(min_page_allocated(li,s))