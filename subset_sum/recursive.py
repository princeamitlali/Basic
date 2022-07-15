import time
curr = []
count = 0
su = 0
def substring_generator(s,curr,i=0):
    if i == len(s):
        print(curr)
        if sum(curr) == su:
            global count
            count += 1
        curr = []
        return []
    substring_generator(s,curr,i+1)
    substring_generator(s,curr + [s[i]],i+1)
    
    
 
def time_taken(s): 
    start = time.time()
    val = substring_generator(s,[],0)
    end = time.time()  
    
    print("frequency is {1} ".format(n,count))
    print()
    print("time diffrence is {0}".format(end - start))

n = list(map(int,input("enter elements ").split(",")))

su = int(input("enter the sum :: "))

time_taken(n)


"""
time and space complexity is O(d) where d is the number of digits in n
"""


            


