class Queue:
    def __init__(self, max_size) -> None:
        self.max_size = max_size - 1
        self.elements = []
        # self.print_queue()
        # return self.elements

    def insert_rear(self, val):
        if self.is_full():
            print("Queue is Full")
            self.print_queue()
            return None
        self.elements.insert(0, val)
        self.print_queue()
        return val

    def delete_front(self):
        if self.is_empty():
            print("Queue is empty")
            self.print_queue()
            return None
        self.print_queue()
        return self.elements.pop(-1)

    def insert_front(self, val):
        if self.is_full():
            print("Queue is Full")
            self.print_queue()
            return None
        self.elements.append(val)
        self.print_queue()
        return val

    def size(self):
        return len(self.elements)

    def delete_rear(self):
        if self.is_empty():
            print("Queue is empty")
            self.print_queue()
            return None
        self.print_queue()
        return self.elements.pop(0)

    def get_front(self):
        if self.is_empty():
            print("Queue is empty")
            self.print_queue()
            return None
        self.print_queue()
        return self.elements[-1]

    def get_rear(self):
        if self.is_empty():
            print("Queue is empty")
            self.print_queue()
            return None
        self.print_queue()
        return self.elements[0]

    def is_full(self):
        return self.size() == self.max_size

    def is_empty(self):
        return self.size() == 0
    
    def print_queue(self):
        print(self.elements)


queue = Queue(3)
queue.insert_front(1)
queue.insert_rear(2)
queue.insert_front(3)
queue.insert_rear(4)
queue.insert_front(5)

queue.get_front()
queue.get_rear()
queue.delete_front()

queue.get_front()
queue.get_rear()
queue.delete_rear()
queue.delete_front()
queue.delete_rear()
queue.get_front()
queue.get_rear()
