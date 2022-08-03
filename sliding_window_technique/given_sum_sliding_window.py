li = [1,4,20,3,10,5]

given_sum = 33

su = 0
start = 0
end = 0
for i in range(len(li)):
    if su < given_sum:
        su += li[i]
        #print(su)
    while su > given_sum and start < len(li):
        su -= li[start]
        start += 1
        #print(su)
    if su == given_sum:
        print(li[start:i+1])
        break
