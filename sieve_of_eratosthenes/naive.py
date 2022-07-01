
import time
import supporting.check_prime as cp
ls = []

def primeLessThanNumber(num):
    for i in range(2,num):
        if cp.isPrime(i):
            ls.append(i)
            
def time_taken(ip): 
    start = time.time()
    print("prime numbers less than {0} is :".format(ip))
    primeLessThanNumber(ip)
    end = time.time()  
    print("time diffrence is {0}".format(end - start))

num = int(input("enter number "))

time_taken(num)
print(ls)

            