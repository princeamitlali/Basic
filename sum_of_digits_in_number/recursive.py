import time


def sum_of_digits(n):
    sum = 0
    if n == 0:
        return 0
    return sum_of_digits(n//10) + n % 10
        
        
    
def time_taken(n): 
    start = time.time()
    val = sum_of_digits(n)
    end = time.time()  
    
    print("{0} sum of digits ::::: {1}".format(n,val))
    print()
    print("time diffrence is {0}".format(end - start))

n = int(input("enter number "))


time_taken(n)


"""
time and space complexity is O(d) where d is the number of digits in n
"""


            