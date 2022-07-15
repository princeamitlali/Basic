import time
count = 0
su = 0
def substring_generator(s,curr,su):
    if curr == 0:
        if su == 0:
            return 1
        else:
            return 0
    return substring_generator(s,curr-1,su) + substring_generator(s,curr-1,su - s[curr-1])
    
    
 
def time_taken(s): 
    start = time.time()
    val = substring_generator(s,len(s),su)
    end = time.time()  
    
    print("frequency is {1} ".format(n,val))
    print()
    print("time diffrence is {0}".format(end - start))

n = list(map(int,input("enter elements ").split(",")))

su = int(input("enter the sum :: "))

time_taken(n)


"""
time and space complexity is O(d) where d is the number of digits in n
"""


            


