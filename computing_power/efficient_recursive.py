import time


def pow(num,power):
    if power == 0:
        return 1
    temp = pow(num,power//2)
    temp *= temp
    if power %2 == 0:
        return temp
    else:
        return temp*num 
def time_taken(num,power): 
    start = time.time()
    val = pow(num,power)
    end = time.time()  
    
    print("{0} raise to the power {1} = {2}".format(num,power,val))
    print()
    print("time diffrence is {0}".format(end - start))

num = int(input("enter number "))
power = int(input("Enter Power ::"))

time_taken(num,power)


            