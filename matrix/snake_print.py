li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

dir = False

for i in li:
    # print(i)
    if dir:
        i = i[::-1]
        dir = False
    else:
        dir = True
    for j in i:
        print(j,end=" ")