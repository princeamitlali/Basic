
import time
def factorial(digit):
    if digit == 0 or digit == 1:
        return 1
    return digit * factorial(digit-1)
    

digit = int(input("enter number "))
start = time.time()
print("factorial of {0} is  {1}".format(digit,factorial(digit)))
end = time.time()
print("time diffrence is {0}".format(end - start))

