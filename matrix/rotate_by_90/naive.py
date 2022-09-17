"""
the first row will become the column and vice-versa
"""
li = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print(li)
n = len(li[0])-1

temp = []
while n > -1:
    t = []
    for i in range(len(li)):
        t.append(li[i][n])
    n -= 1
    temp.append(t)
    print(t)
print(temp)
    