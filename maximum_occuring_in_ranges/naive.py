ranges = [[1,5],[2,6],[3,7],[4,8],[5,9]]
low = ranges[0][0]
high =ranges[0][1]

from collections import defaultdict

de = defaultdict(int)

for start,end in ranges:
    for i in range(start,end+1):
        de[i] = de[i] + 1

maxi = 0
val = 0

for key in de:
    if de[key] > maxi:
        maxi = de[key]
        val = key
print(val)