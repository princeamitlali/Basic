import time


def sum_of_digits(n):
    return sum(list(map(int,str(n).strip())))
        
        
    
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


            