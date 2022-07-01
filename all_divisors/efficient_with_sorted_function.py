from math import ceil, sqrt
import time
ls = []

def allDivisors(digit):
    for i in range(1,ceil(sqrt(digit))):
        if digit % i == 0:
            ls.append(i)
            if i != digit/i:
                ls.append(digit//i)
    return sorted(ls)
def time_taken(ip): 
    start = time.time()
    val = allDivisors(ip)
    end = time.time()  
    print("time diffrence is {0}".format(end - start))
    print("divisors of {0} is {1}:".format(digit,val))

digit = int(input("enter number "))

time_taken(digit)




            