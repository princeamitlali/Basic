
def count_digit(digit):
    count = 0
    while digit != 0:
        count += 1
        digit = digit //10
    print("Digit Count is {0}".format(count))
    
digit = int(input("enter a number to find the numbers of digit in it "))
count_digit(digit)