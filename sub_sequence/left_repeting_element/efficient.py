def left_most_repeating(s):
    arr = [-1 for i in range(26)]
    for i in s:
        v = ord(i)-97
        arr[v] = arr[v] + 1
    for i in range(len(s)):
        val = ord(s[i]) -97
        if arr[val] > 0:
            return i
    return -1
print(left_most_repeating('teekforgeeks'))
    