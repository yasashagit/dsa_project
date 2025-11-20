# Array data structure
class Array:
    def __init__(self, initial=None):
        self.data = initial if initial else []

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        return None

    def search(self, value):
        for i, v in enumerate(self.data):
            if v == value:
                return i
        return -1

    def __str__(self):
        return str(self.data)
    
# List data structure
class List:
    def __init__(self, initial=None):
        self.data = list(initial) if initial else []

    def insert(self, index, value):
        self.data.insert(index, value)

    def append(self, value):
        self.data.append(value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        return None

    def search(self, value):
        for i, v in enumerate(self.data):
            if v == value:
                return i
        return -1

    def length(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)


# Linked list data structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def delete(self, value):
        if not self.head:
            return False

        if self.head.value == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " → ".join(values)

# Stack data structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "Stack(top→bottom): " + str(list(reversed(self.items)))


# Queue data structure
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "Queue(front→rear): " + str(list(self.items))
