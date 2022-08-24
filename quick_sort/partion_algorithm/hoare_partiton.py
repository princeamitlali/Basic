
li = [5,3,8,4,2,7,1,10]

pivot = li[0]
print(li)

low = -1
high = len(li) 

while True:
    low += 1
    while li[low] < pivot:
        low +=1
    
    high -= 1
    while li[high] > pivot:
        high -=1
    if low >= high:
        break 
    temp = li[low]
    li[low] = li[high]
    li[high] = temp
    
    
print(li)