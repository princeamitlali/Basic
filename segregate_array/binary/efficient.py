li = [1,0,0,1,1,0,1,0,1]


def partation(li,low,high):
    low -= 1
    high += 1
   
    pivot = 0

    while True:
        low += 1
        while li[low] == pivot:
            low +=1
        
        high -= 1
        while li[high] == 1:
            high -=1
        if low >= high:
            return 
        temp = li[low]
        li[low] = li[high]
        li[high] = temp


partation(li,0,len(li)-1)
print(li)