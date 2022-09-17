li = [[10,20,30,40],
[15,25,35,45],
[27,29,37,48],
[32,33,39,50]
]

found = 56

def search(li,found):
    if found < li[0][0] or found > li[-1][-1]:
        print("not found")
        return
    r = 0
    c = len(li[0]) -1
    
    while r < len(li) and c > -1:
        val = li[r][c]
        print(val)
        if val == found:
            print(r,c)
            return 
        if found < val:
            c -= 1
        else:
            r += 1
    
    print("not found")
    return 
search(li,found)