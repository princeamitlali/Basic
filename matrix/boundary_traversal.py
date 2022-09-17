
li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
v = len(li)
print(v)


if 3> v > 0:
    for i in li[0]:
        print(i,end=" ")
else:
    for i in li[0][:-1]:
        print(i,end=" ")

# print(li[0][:-1])
if v >2:
    for i in li:
        print(i[-1],end=" ")
        
if v == 2:
    for i in li[-1][::-1]:
        print(i,end= " ")
elif v>=3:
    for i in li[-1][::-1][1:-1]:
        print(i,end= " ")

if v > 2:
    n = len(li)
    for i in range(n-1):
        print(li[n-i-1][0],end =" ")
