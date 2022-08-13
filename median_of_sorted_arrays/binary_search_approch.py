li = [0,2,4,6,8]
li2 = [1,3,5,7,9]

def median(li,li2):
    n1 = len(li)
    n2 = len(li2)
    begin1 = 0
    end1 = n1
    while begin1 <= end1 :
        i1 = (begin1 + end1)//2
        i2 = (n1 +n2 +1) //2 - i1
        min1 = 99999999 if i1 == n1 else li[i1]
        max1 = -99999999999 if i1 == 0 else  li[i1-1]
        min2 =  999999999999 if i2==n2 else  li2[i2]
        max2 = -999999999999  if i2==0 else li2[i2-1] 
        
        if max1 <= min2 and max2 <= min1 :
            if (n1 + n2) % 2 == 0:
                return (max(max1,max2) + min(min1,min2)) /2
            else:
                return max(max1,max2)
        else:
            if max1 > min2 :
                end1 = i1 -1
            else:
                begin1 = i1 + 1
                
print(median(li,li2))