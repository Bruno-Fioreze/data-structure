class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        self._size = 0
    
    def increment_size(self):
        self._size += 1
    
    def append(self, number):
        node = Node(number)
        if not self.head:
            self.head = node
            self.last_node = node
            self.increment_size()
            return

        self.increment_size()
        self.last_node.next = node
        self.last_node = node
     
    def __len__(self):
        return self._size
        
numbers = [1, 30, 90, 50, 99]
root = LinkedList()
for number in numbers:
    root.append(number)

print(
    root.head.next.next.next.next
)

print(
    len(root)
)
