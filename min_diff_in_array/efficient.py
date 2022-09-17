li = [1,8,12,5,18]

li = sorted(li, reverse=True)

mini = li[0]

for i in range(len(li)-1):
    mini = min(mini, li[i] - li[i+1])
    
print(mini)