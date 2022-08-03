li = [1,4,20,3,10,5]
k = 3
su = sum(li[0:k])
max_sum = su
print(su)
for i in range(k,len(li)):
    su = su - li[i-k] + li[i]
    print(su)
    if su > max_sum:
        max_sum = su
print(max_sum)