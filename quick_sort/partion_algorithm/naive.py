li = [5,13,6,9,12,11,8]

partion_index = 6
temp = []
partion_element = li[partion_index]
for i in li:
    if i < partion_element:
        temp.append(i)
        
temp.append(partion_element)

for i in li:
    if i > partion_element:
        temp.append(i)
        
li = temp
print(li)
