arr = []
st = ""
s = "welcome to gfG"
for i in s:
    if i == " ":
        arr.append(st)
        st = ""
    st = i + st 
arr.append(st)
print(arr)
print(" ".join(arr)[::-1])