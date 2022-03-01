import time
def factorial(first_num,second_num):
    res = 1
    if first_num != second_num :
        while first_num >second_num-1:
            if first_num == 0:
                first_num -= 1
                continue
            res = res *  first_num
            first_num -= 1
    return res
    
    
first_num = int(input("enter first number "))
second_num = int(input("enter second number "))
if second_num > first_num:
    second_num = first_num + second_num
    first_num = second_num - first_num
    second_num = second_num - first_num
    
start = time.time()
print("factorial is  {0}".format(factorial(first_num,second_num)))
end = time.time()
print("time diffrence is {0}".format(end - start))
            