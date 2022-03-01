import time
def GCD(first,second):
    sub_val = abs(first-second)
    res = min(first,second)
    while res>0:
        if first % res == 0 and second % res == 0:
            break
        res = res - sub_val
    return res

first = int(input("enter first number "))
second = int(input("enter second number "))
start = time.time()
print("GCD of  {0} and {1} is {2}".format(first,second,GCD(first,second)))
end = time.time()
print("execution time = {0}".format(end-start))
        
        