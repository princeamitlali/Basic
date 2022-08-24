li = [8,4,7,9,3,10,5]

def partation(arr,low,high):
    pivot_element = li[high]
    j = low - 1


    for i in range(low,high):
        if li[i] <= pivot_element:
            j += 1
            temp = li[i]
            li[i] = li[j]
            li[j] = temp 
    li[high] = li[j+1]
    li[j+1] = pivot_element
    return j + 1
    # pivot = arr[high]
     
    # # Index of smaller element
    # i = (low - 1)
    # for j in range(low, high):
         
    #     # If current element is smaller than or
    #     # equal to pivot
    #     if (arr[j] <= pivot):
             
    #         # increment index of smaller element
    #         i += 1
    #         arr[i], arr[j] = arr[j], arr[i]
    # arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # return (i + 1)

def quick_sort(li,low,high):
    if low < high :
        partion = partation(li,low,high)
        quick_sort(li,low,partion-1)
        quick_sort(li,partion+1,high)
        
quick_sort(li,0,len(li)-1)

print(li)