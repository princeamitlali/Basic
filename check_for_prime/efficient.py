import time
import math
def isPrime(digit):
    if digit == 1 or digit == 0 :
        return False
    for i in range(2,math.ceil(math.sqrt(digit-1)) ):
        if digit % i == 0:
            return False
    return True

def time_taken(ip): 
    start = time.time()
    print("{0} is Prime {1} :".format(ip,isPrime(ip)))
    end = time.time()  
    print("time diffrence is {0}".format(end - start))

digit = int(input("enter number "))

time_taken(digit)

            