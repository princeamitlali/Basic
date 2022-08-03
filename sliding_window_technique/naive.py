li = [1,4,20,3,10,5]
k = 3
max_sum = li[0]
for i in range(len(li)- k+1):
    su = sum(li[i:i+k])
    print(su)
    if su > max_sum:
        max_sum = su
        
print(max_sum)