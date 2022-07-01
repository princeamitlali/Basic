
import time
temp = []
def sieve(num):
    prime = [True for _ in range(num + 1)]
    last = 0
    p = 2
    while(p*p< num):
        if prime[p]:
            temp.append(p)
            last = p
            for i in range(p*p, num+1,p):
                prime[i] = False
        p += 1
    for j in range(last,num+1):
        if prime[j]:
            temp.append(j)
        
                
            
def time_taken(ip): 
    start = time.time()
    print("prime less than {0} is :".format(ip))
    sieve(ip)
    end = time.time()  
    print("time diffrence is {0}".format(end - start))

num = int(input("enter number "))

time_taken(num)
print(temp)

            