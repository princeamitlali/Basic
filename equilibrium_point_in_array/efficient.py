from re import I
from xml.etree.ElementInclude import FatalIncludeError


li = [2,4,6,-5,15,7]


def is_equilibrium(li):
    total = sum(li)
    print(total)
    l_sum = 0
    for i in li:
        if l_sum == total - i: 
            return True
        l_sum += i 
        total -= i
    return False
        
print(is_equilibrium(li))