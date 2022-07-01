
from math import ceil, sqrt
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
    if digit <= 1: return

    while digit % 2 == 0:
        factors_list.append(2)
        dic[2] = dic[2] + 1
        digit //= 2
    while digit % 3 == 0:
        factors_list.append(3)
        dic[3] = dic[3] + 1
        digit //= 3
    for i in range(5,ceil(sqrt(digit)),6):
        while digit % i == 0:
            factors_list.append(i)
            dic[i] = dic[i] + 1
            digit //= i
        while digit % i+2 == 0:
            factors_list.append(i+2)
            dic[i+2] = dic[i+2] + 1
            digit //= i+2
    if digit > 3:
        factors_list.append(digit)
        dic[digit] = dic[digit] + 1
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

            