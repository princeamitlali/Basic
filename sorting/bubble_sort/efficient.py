li = [10,8,20,5]

def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li)-1-i):
            if li[j]> li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp
    return li
            
print(bubble_sort(li))