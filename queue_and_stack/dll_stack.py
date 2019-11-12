import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self, node = None):
        self.size = 1 if node is not None else 0
        self.node = DoublyLinkedList()

    def push(self, value):
        print("working stack", value)
        self.size += 1
        self.node.add_to_head(value)

    def pop(self):
        if self.size < 1:
            return None
        else:
            self.size -= 1
            return self.node.remove_from_head()

    def len(self):
        return self.size