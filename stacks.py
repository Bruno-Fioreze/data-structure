class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.top = None
        self.last_node = None
        self._size = 0

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r    

    def increment_size(self):
        self._size += 1

    def decrement_size(self):
        self._size += 1

    def push(self, element):
        node = Node(element)
        node.next = self.top
        self.top = node
        self.increment_size()
    
    def pop(self):
        if not self._size:
            raise IndexError("the stack is empty")
        node = self.top
        self.top = self.top.next
        self.decrement_size()
        return node.data

    def peek(self):
        if not self._size:
            raise IndexError("the stack is empty")
        return self.top.data

numbers = [1, 30, 90, 50, 99]
stack = Stack()
for number in numbers:
    stack.push(number)


stack.pop()
stack.pop()

print(
    stack.peek()
)
