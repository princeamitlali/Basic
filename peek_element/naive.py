li = [10]

def peak_element(li):
    if len(li) == 1:
        print(li[0])
    else:
    
        if li[0] >li[1]:
            print(li[0])
        
        if li[len(li)-1] > li[len(li)-2] :
            print(li[len(li)-1])
        
        for i in range(1,len(li)-1):
            if li[i] > li[i -1] and li[i] > li[i+1]:
                print(li[i])
        
        
        

peak_element(li)