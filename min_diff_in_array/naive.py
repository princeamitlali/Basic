li = [1,8,12,5,18]
mini = max(li)
for i in range(len(li)):
    for j in range(i+1,len(li)):
        mini = min(mini,max(li[j]-li[i],li[i]-li[j]))
        
print(mini)