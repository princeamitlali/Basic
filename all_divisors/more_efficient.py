from math import ceil, sqrt
import time
ls = []
rev_ls = []

def allDivisors(digit):
    for i in range(1,ceil(sqrt(digit))):
        if digit % i == 0:
            ls.append(i)
            if i != digit/i:
                rev_ls.append(digit//i)
            
def time_taken(ip): 
    start = time.time()
    allDivisors(ip)
    end = time.time()  
    print("time diffrence is {0}".format(end - start))

digit = int(input("enter number "))

time_taken(digit)
print("divisors of {0} is {1}:".format(digit,ls + rev_ls[::-1]))



            