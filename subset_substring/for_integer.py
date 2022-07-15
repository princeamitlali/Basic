import time
curr = []
def substring_generator(s,curr,i=0):
    if i == len(s):
        print(curr)
        curr = []
        return []
    substring_generator(s,curr,i+1)
    substring_generator(s,curr + [s[i]],i+1)
    
    
 
def time_taken(s): 
    start = time.time()
    val = substring_generator(s,[],0)
    end = time.time()  
    
    #print("{1} max piece possible to cut from rope of lenght {0} ".format(n,val))
    print()
    print("time diffrence is {0}".format(end - start))

n = list(map(int,input("enter elements ").split(",")))



time_taken(n)


"""
time and space complexity is O(d) where d is the number of digits in n
"""


            


