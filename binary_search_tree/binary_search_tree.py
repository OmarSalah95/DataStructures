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
        # greater values become right child
        # if self.value <= value:
        #     if self.right:
        #         self.right.insert(value)
        #     else:
        #         self.right = BinarySearchTree(value)
        # # less than or equal values become left child
        # else:
        #     if self.left:
        #         self.left.insert(value)
        #     else:
        #         self.left = BinarySearchTree(value)

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
        while self.right:
            self = self.right
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # pre-Order
        cache = [node]
        while cache:
            print(cache[0].value)
            if cache[0].left:
                cache.append(cache[0].left)
            if cache[0].right:
                cache.append(cache[0].right)    
            cache.pop(0)
        # # In-Order
        # if cache[0].left:
        #     print(cache[0].left.value)
        # print(cache[0].value)
        # if cache[0].right:
        #     print(cache[0].right.value)
        # # Post-Order
        # if cache[0].left:
        #     print(cache[0].left.value)
        # if cache[0].right:
        #     print(cache[0].right.value)
        # print(cache[0].value)
        
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = [node]
		
        while stack: 
            current = stack.pop()
            if current.left: 
                stack.append(current.left)		
            if current.right:   
                stack.append(current.right)
            print(current.value)
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if not node:
            return
        print(node.value) 
        self.pre_order_dft(node.left) 
        self.pre_order_dft(node.right) 

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if not node:
            return
        self.post_order_dft(node.left) 
        self.post_order_dft(node.right) 
        print(node.value) 
