import collections


li = [10,20,30]

from collections import defaultdict

d = defaultdict(int)

for i in li:
    d[i] += 1

sorted_x = sorted(d.items(), key=lambda kv: kv[1],reverse=True)


if sorted_x[0][1] > len(li)/2:
    print(sorted_x[0])
else:
    print("Not Found")