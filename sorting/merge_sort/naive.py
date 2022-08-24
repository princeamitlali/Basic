li = [10,15,20,20]
li2 = [1,12]

def merge_sort(li,li2):
    for i in li2:
        li.append(i)
    return sorted(li)

print(merge_sort(li,li2))