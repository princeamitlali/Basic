li = [5,4,3,2,1]

def inversion(li):
    count = 0
    n = len(li)
    for i in range(n):
        for j in range(i,n):
            if li[i] > li[j]:
                count += 1
    return count

print(inversion(li))