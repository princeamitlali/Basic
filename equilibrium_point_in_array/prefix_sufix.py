li = [2,4,6,-5,15,7]
li1 = [4,-4,2]


def prefix_sum(arr):
    temp = arr
    for i in range(1,len(temp)):
        temp[i] = temp[i] + temp[i-1]
    return temp
temp = li[::-1]
prefix = prefix_sum(li)
suffix = prefix_sum(temp)[::-1]
#suffix = suffix[::-1]

for i in range(len(li)):
    if prefix[i] == suffix[i]:
        print("yes")


