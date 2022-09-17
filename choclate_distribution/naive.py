li = [7,3,2,8,9,12,56]

m = 3


def min_diff(li,m):
    if m > len(li):
        print("Not Possible")
        return -1


    li = sorted(li)
    mini = li[-1]
    for i in range(0,len(li)- m):
        mini = min(mini,li[i+m-1] - li[i])
        
    print(mini)
    return mini

print(min_diff(li,m))