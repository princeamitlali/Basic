import math
def isPrime(digit):
    if digit == 1 or digit == 0 :
        return False
    
    if digit == 2 or digit == 3:
        return True
    
    if digit % 2 == 0 or digit % 3 == 0:
        return False

    for i in range(5,math.ceil(math.sqrt(digit-1)),6 ):
        if digit % i == 0 or digit % (i+2) == 0:
            return False
    return True
