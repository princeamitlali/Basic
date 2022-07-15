import time


def is_palindrome(s):
    s2 = ""
    for i in range(len(s)-1,-1,-1):
        print(i)
        s2 += s[i]
    if s == s2:
        return True
    return False
        
    
def time_taken(s): 
    start = time.time()
    val = is_palindrome(s)
    end = time.time()  
    
    print("{0} is palindrome ::::: {1}".format(s,val))
    print()
    print("time diffrence is {0}".format(end - start))

s = input("enter String ")


time_taken(s)


"""
time and space complexity is O(n)
"""


            