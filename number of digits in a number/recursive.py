
def count_digit(digit):
    if digit == 0:
        return 0
    return 1 + count_digit(digit//10)

    
digit = int(input("enter a number to find the numbers of digit in it "))
#45ans = count_digit(digit)
print("Digit Count is {0}".format(count_digit(digit)))