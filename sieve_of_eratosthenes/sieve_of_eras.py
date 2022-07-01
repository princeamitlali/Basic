
import time
import supporting.check_prime as cp
ls = []
temp = []
def sieve(num):
    prime = [True for _ in range(num + 1)]
    p = 2
    while(p*p< num):
        if prime[p]:
            for i in range(p*p, num+1,p):
                prime[i] = False
        p += 1
        
    for p in range(2,num+1):
        if prime[p]:
            temp.append(p)
                
            
def time_taken(ip): 
    start = time.time()
    print("prime numbers less than {0} is :".format(ip))
    sieve(ip)
    end = time.time()  
    print("time diffrence is {0}".format(end - start))

num = int(input("enter number "))

time_taken(num)
print(temp)

            