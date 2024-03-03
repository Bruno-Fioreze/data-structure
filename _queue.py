class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self._size = 0
        self.first = None
        self.last = None

    def __repr__(self):
        r = "Empty Queue"
        if self._size:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            
        return r

    def __len__(self):
        return self._size

    def increment_size(self):
        self._size += 1

    def decrement_size(self):
        self._size += 1

    def push(self, element):
        node = Node(element)
        if not self.last:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        
        if not self.first:
            self.first = node
        
        self.increment_size()
    
    def pop(self):
        if self._size:
            elem = self.first.data
            self.first = self.first.next
            self.decrement_size()
            return elem
        raise IndexError("The Queue is empty")

    def peek(self):
        if self._size:
            elem = self.first.data
            return elem
        raise IndexError("The Queue is empty")

numbers = [1, 30, 90, 50, 99]
q = Queue()
for number in numbers:
    q.push(number)

print(
    q
)