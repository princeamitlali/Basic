import time
def surviver(n,m):
    if n == 1:
        return 0
    return (surviver(n-1,m) + m ) % n
    
def time_taken(n,m): 
    start = time.time()
    val = surviver(n,m)
    end = time.time()  
    
    print("{1} person will survive  ".format(n,val))
    print()
    print("time diffrence is {0}".format(end - start))

n = int(input("enter number of person :: "))
m = int(input("enter starting position ::  "))




time_taken(n,m)


"""
time and space complexity is O(d) where d is the number of digits in n
"""


            


