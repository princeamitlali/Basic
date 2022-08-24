li = [8,4,7,9,3,10,5]

def partation(li,low,high):
    low -= 1
    high += 1
   
    pivot = li[low + 1]

    while True:
        low += 1
        while li[low] < pivot:
            low +=1
        
        high -= 1
        while li[high] > pivot:
            high -=1
        if low >= high:
            return high
        temp = li[low]
        li[low] = li[high]
        li[high] = temp
        
   

def quick_sort(li,low,high):
    if low < high :
        partion = partation(li,low,high)
        quick_sort(li,low,partion)
        quick_sort(li,partion+1,high)
        
quick_sort(li,0,len(li)-1)

print(li)