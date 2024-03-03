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

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r    

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
    
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer
    
    def __getitem__(self, index):
        pointer = self._getnode(index)
        if not pointer:
            raise IndexError("list index out of range")  
        return pointer.data
    
    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if not pointer:
            raise IndexError("list index out of range")

        pointer.data = elem

    def index(self, element):
        pointer = self.head
        for i in range(self._size):
            if pointer.data == element:
                return i
            pointer = pointer.next
        raise IndexError(f"{element} is not in list")

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def remove(self, elem):
        if self.head == None:
            raise ValueError(f"{elem} is not in list")
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in list".format(elem))

numbers = [1, 30, 90, 50, 99]
root = LinkedList()
for number in numbers:
    root.append(number)

print(
    root.head.next.next.next.next
)

