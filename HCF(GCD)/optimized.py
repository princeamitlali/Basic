import time
def GCD(first,second):
    while first != second:
        if second == 0:
            return first
        else:
            return GCD(second,first%second)

first = int(input("enter first number "))
second = int(input("enter second number "))
start = time.time()
print("GCD of  {0} and {1} is {2}".format(first,second,GCD(first,second)))
end = time.time()
print("execution time = {0}".format(end-start))