li = [[10,20,30,40],
[15,25,35,45],
[27,29,37,48],
[32,33,39,50]
]

found = 29
flaag = True
for i in range(len(li)):
    for j in range(len(li[0])):
        if li[i][j] ==  found:
            flaag = False
            print(i,j)
            break
        
if flaag:
    print("not found")