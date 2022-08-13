from audioop import lin2adpcm


li1 = [0,1,3,5,7,9]
li2 = [2,4,6,8]

el = 0
com = True
i = 0
while(True):
    print(i,el)
    if el > len(li1)-1:
        com = False
        break
    if i > len(li2)-1:
        break
    if li2[i] > li1[el]:
        li2.insert(i,li1[el])
        el += 1
        i -= 1
    i += 1
        
    
if com:
    for i in range(el,len(li1)):
        li2.append(li1[i])
        
n = len(li2)
if n % 2 == 0:
    print((li2[n//2] + li2[n//2 - 1])/2)
else:
    print(li2[n//2 ])