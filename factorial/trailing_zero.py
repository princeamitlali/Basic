
import time
def trailing_zeros(digit):
    i = 5
    res = 0
    while (i<= digit):
        res = res + digit//i
        i *= 5
    return res
        
    
    

digit = int(input("enter number "))
start = time.time()
print("trailing zeroes in  {0} is  {1}".format(digit,trailing_zeros(digit)))
end = time.time()
print("time diffrence is {0}".format(end - start))

