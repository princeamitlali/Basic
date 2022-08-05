li = [1,2,3,4,5,6,7,8,9]

given_sum = 128

def pair(li,given_sum):
    
    for i in range(len(li)):
        low = i
        high= len(li)-1
        while high >= low:
            sum_now =li[high] + li[low] + li[i]
            if  sum_now== given_sum:
                return li[low],li[high],li[i]
            if sum_now > given_sum:
                high -=1
            else:
                low += 1
                
        return -1
            
print(pair(li,given_sum))