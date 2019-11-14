class Heap:
    def __init__(self, comparator):
        self.storage = []
        if comparator is None:
            self.comparator = lambda parent, child: parent > child
        else:
            self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        root = self.storage[-1]
        del self.storage[-1]
        self._sift_down(0)
        return root

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
    def swap(self, a, b):
        self.storage[a], self.storage[b] = self.storage[b], self.storage[a]
