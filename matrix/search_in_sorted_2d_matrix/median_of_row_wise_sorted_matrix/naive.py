li = [
[1,10,20],
[15,25,30],
[5,8,40]
]

temp = []

for i in li:
    for j in i:
        temp.append(j)
        
temp = sorted(temp)

if len(temp)% 2  != 0:
    print(temp[len(temp)//2 ])
else:
    print((temp[len(temp)//2]+temp[len(temp)//2 + 1])/2)