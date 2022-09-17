li = [1,0,0,1,1,0,1,0,1]


def partation(arr,low,high):
    pivot_element = 0
    j = low - 1


    for i in range(low,high):
        if li[i] == pivot_element:
            j += 1
            temp = li[i]
            li[i] = li[j]
            li[j] = temp 
    temp = li[high]
    li[high] = li[j+1]
    li[j+1] = temp
    return 


partation(li,0,len(li)-1)
print(li)