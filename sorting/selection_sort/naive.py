li= [10,8,20,5]
temp = []

def selection_sort(li):
    for i in range(len(li)):
        mi = 0
        
        for j in range(len(li)):
            if li[j] < li[mi]:
                mi = j
        temp.append(li[mi])
        li[mi] = 99999999999
    return temp

print(selection_sort(li))
    
   