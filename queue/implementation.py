class Queue():
    def __init__(self,max_size) -> None:
        self.max_size = max_size -1
        self.elements = []
        # return self.elements
    
    def enque(self,val):
        if self.size() <= self.max_size:
            self.elements.append(val)
            return val
        print("Queue is Full")
        return None
    
    def size(self):
        return len(self.elements)
    
    def deque(self):
        if self.size() > 0:
            return self.elements.pop(0)
        print("Queue is empty")
        return None
    
    def get_rear(self):
        if self.size() > 0:
            return self.elements[-1]
        print("Queue is empty")
        return None
    def get_front(self):
        if self.size() > 0:
    
            return self.elements[0]
        print("Queue is empty")
        return None
    
queue = Queue(3)
print(queue)
print(queue.enque(1))
print(queue.enque(2))
print(queue.enque(3))
print(queue.enque(4))
print(queue.enque(5))

print(queue.get_rear())
print(queue.get_front())
print(queue.deque())

print(queue.get_rear())
print(queue.get_front())
print(queue.deque())
print(queue.deque())
print(queue.deque())
print(queue.get_rear())
print(queue.get_front())