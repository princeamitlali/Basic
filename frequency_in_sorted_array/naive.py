li = [10,20,30]

freq = 0
checked = li[0]
i = 0
while i < len(li):
    checked = li[i]
    while i<len(li) and checked == li[i]:
        freq += 1
        i += 1
    print(checked,freq)
    freq = 0
    