val = 36

def sqrt(val):
    for i in range(val):
        if i*i == val:  
            return i
        elif i*i > val:
            return i -1
        
print(sqrt(val))