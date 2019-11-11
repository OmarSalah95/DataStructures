from doubly_linked_list import DoublyLinkedList
class LRUCache:
    def __init__(self, limit=10):
        self.list = DoublyLinkedList()
        self.dict = {}
        self.limit = limit

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]

            self.list.delete(node)
            self.list.add_to_head(node)
            return node.value
        else:
            return None

    def set(self, key, value):
        if key in self.dict:
            node = self.dict[key]
            node.value = value

            if self.list.head is not node:
                self.list.delete(node)
                self.list.add_to_head(node)
        else:
            new_node = DoublyLinkedList(value)
            if self.list.get_max() == self.limit:
                self.dict.pop(key)
                self.list.delete(node)
            self.list.add_to_head(new_node)
            self.dict[key] = new_node
