li = [1,2,3,4,5]

def bubble_sort(li):
    no_change = True
    for i in range(len(li)):
        for j in range(len(li)-1-i):
            if li[j]> li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp
                no_change = False
        if no_change:
            break
    return li
            
print(bubble_sort(li))