import time
def LCM(first,second):
    res = max(first,second)
    add_val = res
    while res>0:
        if res % first  == 0 and res % second  == 0:
            break
        res = res + add_val
    return res

first = int(input("enter first number "))
second = int(input("enter second number "))
start = time.time()
print("LCM of  {0} and {1} is {2}".format(first,second,LCM(first,second)))
end = time.time()
print("execution time = {0}".format(end-start))
        
        