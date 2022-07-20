li = [1,2,3,4,5,6,5,4,3,9,11,2]

lar,sec = li[0],li[1]
for i in li:
    if i > lar:
        sec = lar
        lar = i
                  
print(sec)
    