import time
sub = []

def swap(i,j):
    return j,i

def permute(s,curr=0):
    if curr == len(s)-1:
        print("".join(s))
    for i in range(curr,len(s),1):
        temp = s[i]
        s[i] = s[curr]
        s[curr] = temp
        permute(s,curr+1)
        temp = s[i]
        s[i] = s[curr]
        s[curr] = temp

        
    
    
 
def time_taken(s): 
    start = time.time()
    st = list(s)
    val = permute(st)
    end = time.time()  
    
    #print("{1} max piece possible to cut from rope of lenght {0} ".format(n,val))
    print()
    print("time diffrence is {0}".format(end - start))

n = input("enter String ")




time_taken(n)


"""
time and space complexity is O(d) where d is the number of digits in n
"""


            


