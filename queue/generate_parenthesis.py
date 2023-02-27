# n = 3

# s = ["(",")"]
# for i in range(n *2 - 1):
#     temp = []
#     while len(s) > 0:
#         res = s.pop(0)
#         temp.append(res + ")")
#         temp.append(res + "(")
#     s = temp
#     # print(s)
# res = []
# # s = ["()()()"]
# for i in s:
#     stack = []
#     flag = True
#     for j in i:
#         if j == "(":
#             stack.append("(")
#         if j == ")":
#             if len(stack) == 0 :
               
#                 flag = False
#                 break
#             elif stack.pop() != "(":
#                 print("here")
#                 flag = False
#                 break
#     if len(stack)==0 and flag:
#         res.append(i)
# print(res)


import itertools
minu = [0,1,2,3,4,5]
hr = [0,1,2,3]
a = [[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5]]
print(len(list(itertools.product(*a))))