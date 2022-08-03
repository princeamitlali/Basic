li = [10,10,10,20,30]

freq = 0
checked = li[0]
i = 0
flag = True
while i < len(li):
    checked = li[i]
    while i<len(li) and checked == li[i]:
        freq += 1
        i += 1
    if freq > len(li)/2:
        print("majority element with frequency")
        print(checked,freq)
        print("index is",i-1)
        flag = False
    freq = 0
    
if flag:
    print("No majority element found")