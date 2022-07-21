li = [1,2,3,4,5]
shift_by = 8

#shift_by %=  len(li)
#li = li[shift_by:] + li[:shift_by]

li = li[shift_by%len(li):] + li[:shift_by%len(li)]



print(li)