import time
ls = []

def allDivisors(digit):
    for i in range(2,digit):
        if digit % i == 0:
            ls.append(i)
            
def time_taken(ip): 
    start = time.time()
    allDivisors(ip)
    end = time.time()  
    print("time diffrence is {0}".format(end - start))

digit = int(input("enter number "))

time_taken(digit)
print("divisors of {0} is {1}:".format(digit,ls))



            