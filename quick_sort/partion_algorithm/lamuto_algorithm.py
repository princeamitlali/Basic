li = [70,60,80,40,30]
pivot_index = 2


pivot_element = li[pivot_index]

li[pivot_index] = li[-1]
li[-1] = pivot_element

low = -1

for i in range(len(li)):
    if li[i] < pivot_element:
        low += 1
        temp = li[i]
        li[i] = li[low]
        li[low] = temp 
        
li[-1] = li[low+1]
li[low+1] = pivot_element
print(li)       