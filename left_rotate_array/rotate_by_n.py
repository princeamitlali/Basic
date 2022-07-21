li = [1,2,3,4,5]
shift_by = 8
shift_by %= len(li)

val = []

for i in range(shift_by,len(li)):
    val.append(li[i])
    
for i in range(shift_by):
    val.append(li[i])
    
print(val)