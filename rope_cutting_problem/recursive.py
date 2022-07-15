import time

def cut_rope(r,a,b,c):
    if r == 0:
        return 0
    if r < 0 :
        return -1
    
    res = max(cut_rope(r-a,a,b,c),cut_rope(r-b,a,b,c),cut_rope(r-c,a,b,c))
    
    if res == -1:
        return -1
    return res + 1
 
def time_taken(n,a,b,c): 
    start = time.time()
    val = cut_rope(n,a,b,c)
    end = time.time()  
    
    print("{1} max piece possible to cut from rope of lenght {0} ".format(n,val))
    print()
    print("time diffrence is {0}".format(end - start))

n = int(input("enter rope length "))
a = int(input("enter length 1 "))
b = int(input("enter length  2 "))
c = int(input("enter length 3  "))



time_taken(n,a,b,c)


"""
time and space complexity is O(d) where d is the number of digits in n
"""


            



def cut_rope(r,a,b,c):
    if r == 0:
        return 1
    if r < 0 :
        return 1
    
    res = max(cut_rope(r-a,a,b,c),cut_rope(r-b,a,b,c),cut_rope(r-c,a,b,c))
    
    if res == -1:
        return res
    return res + 1

