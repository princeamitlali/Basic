class Stack:
    
    def __init__(self) -> None:
        self.elements = []
    def push(self,val):
        self.elements.append(val)
        return self.elements
    def is_empty(self):
        return len(self.elements) == 0
    def peek(self):
        if self.is_empty():
            print("No element present")
            return None
        return self.elements[-1]
    def pop(self):
        if self.is_empty():
            return None
        return self.elements.pop()
    
    
stack = Stack()
print(stack)
print(stack.peek())
print(stack.pop())
print(stack.push(2))
print(stack)
print(stack.push(3))
print(stack)
print(stack.peek())
print(stack.pop)