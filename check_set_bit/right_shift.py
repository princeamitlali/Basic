import time


def is_set(num,posit):
    if num & ( num >> (posit -1)) == 1:
        return True
    return False
def time_taken(num,posit): 
    start = time.time()
    val = is_set(num,posit)
    end = time.time()  
    
    print("{0} th bit of {1} is set :::: = {2}".format(posit,num,val))
    print()
    print("time diffrence is {0}".format(end - start))

num = int(input("enter number "))
power = int(input("Enter bit position ::"))

time_taken(num,power)


            