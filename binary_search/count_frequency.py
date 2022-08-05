from first_occurance_iterative import *
from last_occurance_iterative import *

li = [1,2,3,4,5,6,6,6,6,6,7]
to_find = 6

def find_freq(li,to_find):
    f = first_occurance(li,to_find)
    if f == -1:
        print("Do not exist")
    else:
        print(last_occurance(li,to_find) - f + 1)
        
find_freq(li,to_find)