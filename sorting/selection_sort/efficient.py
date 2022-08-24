li= [10,8,20,5]
temp = []

def selection_sort(li):
    for i in range(len(li)):
        mini = i
        
        for j in range(i,len(li)):
            if li[j] < li[mini]:
                mini = j
        print(li)
        temp = li[i]
        li[i] = li[mini]
        li[mini] = temp
    return li

print(selection_sort(li))
    
   