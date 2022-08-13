from asyncio.windows_events import INFINITE


li = [10,20,30,40]
s= 2

def min_pages_allocated(li,n,s):
    if s == 1:
        return sum(li[:n-1])
    if n == 1:
        return li[0]
    
    res = 999999999999999
    
    for i in range(1,n):
        res = min(res,max(min_pages_allocated(li,i,s-1),sum(li[i:])))
        print(res)
    return res
        
print(min_pages_allocated(li,len(li),s))