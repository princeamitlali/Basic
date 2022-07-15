from itertools import permutations

import time

def permute(s,curr=0):
    pl = permutations(s)
    for perm in list(pl):
         print (''.join(perm))
        
    
    
 
def time_taken(s): 
    start = time.time()
    st = list(s)
    permute(st)
    end = time.time()  
    
    #print("{1} are permutations of  {0} ".format(n,val))
    print()
    print("time diffrence is {0}".format(end - start))

n = input("enter String ")




time_taken(n)


"""
time and space complexity is O(d) where d is the number of digits in n
"""


            


