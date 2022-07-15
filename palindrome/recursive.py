import time


def is_palindrome(num,start,end):
    if start >= end :
        return True
    return (num[start] == num[end] ) and is_palindrome(num,start +1 , end - 1)
    
def time_taken(s): 
    start = time.time()
    val = is_palindrome(s,0, len(s)-1)
    end = time.time()  
    
    print("{0} is palindrome ::::: {1}".format(s,val))
    print()
    print("time diffrence is {0}".format(end - start))

s = input("enter String ")


time_taken(s)


"""
time and space complexity is O(n)
"""


            