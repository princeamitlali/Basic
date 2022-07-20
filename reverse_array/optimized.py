li = [1,2,3,4,5,6]

start = 0
end = len(li) -1


while end > start:
    temp = li[start]
    li[start] = li[end]
    li[end] = temp
    start += 1
    end -= 1

print(li)
    