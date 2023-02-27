'''
convert from infix to postfix
'''

Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

def in_to_pre(expression:str)-> str:
    expression = expression[::-1]
    stack = [] # initialization of empty stack
    output = '' 
    
    for character in expression:
        if character not in Operators:  # if an operand append in postfix expression
            output+= character
        elif character==')':  # else Operators push onto stack
            stack.append(')')
        elif character=='(':
            while stack and stack[-1]!= ')':
                output+=stack.pop()
            stack.pop()
        else: 
            while stack and stack[-1]!=')' and Priority[character]<=Priority[stack[-1]]:
                output+=stack.pop()
            stack.append(character)
    while stack:
        output+=stack.pop()
    return output[::-1]

def evaluation(exp)-> int:
    s = []
    exp =exp[::-1]
    for i in exp:
        if i in Operators:
            res = int(s.pop())
            if i is "+":
                res += int(s.pop())
            if i is "-":
                res -= int(s.pop())
            if i is "*":
                res *= int(s.pop())
            if i is "/":
                res /= int(s.pop())
            if i is "^":
                res ^= int(s.pop())
            s.append(res)
        else:
            s.append(i)
    return s[-1]
post = in_to_pre("(2+3)*5")
print(post)
print(evaluation(post))