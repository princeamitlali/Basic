from math import factorial
import time
from collections import defaultdict
import supporting.check_prime as cp

factors_list = []
dic = defaultdict(int)

def print_dic(dic,digi):
    l = len(dic)
    for i in dic:
        print(str(i) + " X " + str(dic[i]), end=" ")
        l -=1
        if l > 0 :
            print(" + ", end=" ")
    print(" = ",str(digi))

def primeFactors(digit):
    for i in range(2,digit):
        if cp.isPrime(i):
            x = i
            while digit % x == 0:
                factors_list.append(i)
                dic[i] = dic[i] + 1
                x = x * i
def time_taken(ip): 
    start = time.time()
    print("prime factors of {0} is :".format(ip))
    primeFactors(ip)
    end = time.time()  
    print("time diffrence is {0}".format(end - start))

digit = int(input("enter number "))

time_taken(digit)
print(factors_list)
print()
print_dic(dic,digit)

            