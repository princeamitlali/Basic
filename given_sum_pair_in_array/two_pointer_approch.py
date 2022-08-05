li = [1,2,3,4,5,6,7,8,9]

given_sum = 12

def pair(li,given_sum):
    low = 0
    high= len(li)-1
    
    while high >= low:
        sum_now =li[high] + li[low]
        if  sum_now== given_sum:
            return li[low],li[high]
        if sum_now > given_sum:
            high -=1
        else:
            low += 1
            
    return -1,-1
            
print(pair(li,given_sum))