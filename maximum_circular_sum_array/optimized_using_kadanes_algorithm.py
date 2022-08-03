li = [8,-4,3,-5,4]

def kadenes_algo(lis):
    res = li[0]
    max_end = li[0]
    for i in range(1,len(li)):
        max_end = max(li[i],max_end + li[i])
        res = max(res,max_end)
    return res

normal_sub_sum = kadenes_algo(li)
print("normal",normal_sub_sum)

total_sum = sum(li)

li = [-i for i in li]
print(li)
# max_circular_sum = 
real_max = max(normal_sub_sum,total_sum + kadenes_algo(li))

print(real_max)