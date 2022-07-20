from itertools import permutations

def permute(s,curr=0):
    pl = permutations(s)
    for perm in list(pl):
         print (''.join(perm))
         
n = input("enter String ")

permute(n)


        


