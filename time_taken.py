temp = []
for i in range(35):
    temp.append(len(str(pow(2,i))))
    
print(temp)


num = 1283
l = len(str(num))
print(int("".join(sorted(str(num)))))
dict = {1:[0,3],2:[4,6],3:[7,9],4:[10,13],5:[14,16],6:[17,19],7:[20,23],8:[24,26],9:[27,29],10:[30,33],11:[34,34]}

val = dict[l]
print(val)
for i  in range(val[0],val[1]+1):
    if int("".join(sorted(str(pow(2,i))))) == int("".join(sorted(str(num)))):
        print("found")

print("not")
        