li = [0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1]
count = 0
res = 0
for i in li:
    if i == 0:
        res = max(res,count)
        count = 0
    else:
        count += 1
 
res = max(res,count)       
print(res)

