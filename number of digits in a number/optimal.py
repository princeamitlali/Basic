
import math 



def count_digit(digit):
    return math.floor(math.log10(digit)+1)

    
digit = int(input("enter a number to find the numbers of digit in it "))
#45ans = count_digit(digit)
print("Digit Count is {0}".format(count_digit(digit)))