li = [7,10,4,10,6,5,2]
leader = li[-1]
temp = [li[-1]]
for i in li[::-1]:
    if i > leader:
        leader = i
        temp.append(leader)
        
print(temp[::-1])