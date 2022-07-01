import time

def isPrime(digit):
    if digit == 0 :
        return False
    for i in range(2,digit-1):
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

            