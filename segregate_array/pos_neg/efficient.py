li = [1,-2,3,-4,5,-6,7,-8,9]


def partation(li,low,high):
    low -= 1
    high += 1
   
    pivot = 0

    while True:
        low += 1
        while li[low] < pivot:
            low +=1
        
        high -= 1
        while li[high] > pivot:
            high -=1
        if low >= high:
            return 
        temp = li[low]
        li[low] = li[high]
        li[high] = temp


partation(li,0,len(li)-1)
print(li)