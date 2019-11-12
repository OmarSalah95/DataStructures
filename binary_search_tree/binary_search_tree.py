import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        while self:
            if value < self.value and self.left is None:
                self.left = BinarySearchTree(value)
                break
            elif value < self.value and self.left is not None:
                self = self.left
            elif value >= self.value and self.right is None:
                self.right = BinarySearchTree(value)
                break
            else:
                self = self.right
            # The recursive version below also works.
            
            
            # if value < self.value and self.left is None:
            #   self.left = BinarySearchTree(value)
            # elif value < self.value and self.left is not None:
            #   self.left.insert(value)
            # elif value >= self.value and self.right is None:
            #   self.right = BinarySearchTree(value)
            # else:
            #   self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not   
    def contains(self, target):
        while True:
            if self.value == target:
                return True
            elif target < self.value and self.left is None:
                return False
            elif target < self.value and self.left is not None:
                self = self.left
            elif target >= self.value and self.right is None:
                return False
            else:
                self = self.right

    # Return the maximum value found in the tree
    def get_max(self):
        while self:
            if self.right is None:
                return self.value
            else:
                self = self.right

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
