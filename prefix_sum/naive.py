li = [2,8,3,9,6,5,4]

queries = [[0,3],[1,3],[0,6]]

for i in queries:
    su = 0
    for j in range(i[0],i[1]+1):
        su += li[j]
    print(su)