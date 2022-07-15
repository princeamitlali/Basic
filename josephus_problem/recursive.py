import time
def surviver(s,m, curr = 0):
    if len(s) == 1:
        print(s)
        return 0
    curr = (curr -1 + m)%len(s)
    s.pop(curr)
    surviver(s,m,curr)
    
def time_taken(n,m): 
    s = [i for i in range(n)]
    start = time.time()
    val = surviver(s,m,0)
    end = time.time()  
    
    #print("{1} max piece possible to cut from rope of lenght {0} ".format(n,val))
    print()
    print("time diffrence is {0}".format(end - start))

n = int(input("enter number of person :: "))
m = int(input("enter starting position ::  "))




time_taken(n,m)


"""
time and space complexity is O(d) where d is the number of digits in n
"""


            


