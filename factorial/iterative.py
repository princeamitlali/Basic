import time
def factorial(digit):
    res = 1
    if digit != 0 or digit != 1:
        while digit >1:
            res = res *  digit
            digit -= 1
    return res
    
    
digit = int(input("enter number "))
start = time.time()
print("factorial of {0} is  {1}".format(digit,factorial(digit)))
end = time.time()
print("time diffrence is {0}".format(end - start))
            