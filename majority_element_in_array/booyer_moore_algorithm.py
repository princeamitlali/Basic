li = [10,20,30]
res = 0
count = 1
for i in range(len(li)):
    if li[i] == li[res]:
        count += 1
    else:
        count -= 1
    if count == 0:
        res = i
        count = 1

print(li[res])
count = 0
for i in li:
    if i == li[res]:
        count += 1

if count > len(li) /2:
    print(li[res],res)
else:
    print("Not Found")