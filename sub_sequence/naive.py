'''
generate all the subsequence of a string
'''

def sub_seq_generator(s:str) -> list:
    arr = [""]
    for i in s:
        n = len(arr)
        for j in range(n):
            arr.append(arr[j]+i)
    return arr
val = sub_seq_generator("test")
print(val)