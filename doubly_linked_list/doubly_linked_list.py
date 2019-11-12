"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        # list is currently empty
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        # list is currently empty
        if not self.head:
            return None

        old_head = self.head
        # list only has 1 node
        if self.head is self.tail:
            self.head = None
            self.tail = None

        else:
            new_head = self.head.next
            self.head.delete()
            self.head = new_head

        self.length -= 1
        return old_head.value

    def add_to_tail(self, value):
        # list is currently empty
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        # list is currently empty
        if not self.head:
            return None
        old_tail = self.tail
        # list only has 1 node
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            new_tail = self.tail.prev
            self.tail.delete()
            self.tail = new_tail
        self.length -= 1
        return old_tail.value

    def move_to_front(self, node):
        # if node is only item in list OR is already at the front, do nothing
        if self.length > 1 and self.head != node:
            # if node is current tail, make sure to assign new tail
            if node is self.tail:
                self.remove_from_tail()
            else:
                node.delete()
                self.length -= 1
            self.add_to_head(node.value)

    def move_to_end(self, node):
        # if node is only item in list OR is already at the end, do nothing
        if self.length > 1 and self.tail != node:
            # if node is current head, make sure to assign new head
            if node is self.head:
                self.remove_from_head()
            else:
                node.delete()
                self.length -= 1
            self.add_to_tail(node.value)

    def delete(self, node):
        # if node is only item in list:
        if self.length == 1:
            self.head = None
            self.tail = None
        # if node is current head or tail, assign new one before deleting
        if node is self.head:
            self.head = node.next
        elif node is self.tail:
            self.tail = node.prev
        self.length -= 1
        node.delete()

    def get_max(self):
        # list is empty
        if self.length == 0:
            return None

        current_node = self.head
        current_max = self.head.value
        while current_node:  # shorthand for current_node != None
            if current_node.value > current_max:
                current_max = current_node.value
            current_node = current_node.next

        return current_max