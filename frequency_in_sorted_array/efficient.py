li = [1,1,1,3,3,4]

from collections import defaultdict
d = defaultdict(int)
for i in li:
    d[i] = d[i] + 1
    
print(d)