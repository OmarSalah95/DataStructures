import unittest
from lru_cache import LRUCache


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(3)

    def test_cache_overwrite_appropriately(self):
        self.cache.set('item1', 'a') # [{1:a}]
        self.cache.set('item2', 'b') # [{2:b}, {1:a}]
        self.cache.set('item3', 'c') # [{3:c}, {2:b},  {1:a}]

        self.cache.set('item2', 'z') # [{2:z}, {3:c}, {1:a}]

        self.assertEqual(self.cache.get('item1'), 'a') # [{1:a}, {2:z}, {3:c}]
        self.assertEqual(self.cache.get('item2'), 'z') # [{2:z}, {1:a}, {3:c}]

    def test_cache_insertion_and_retrieval(self):
        self.cache.set('item1', 'a') # [{1:a}]
        self.cache.set('item2', 'b') # [{2:b}, {1:a}]
        self.cache.set('item3', 'c') # [{3:c}, {2:b}, {1:a}]

        self.assertEqual(self.cache.get('item1'), 'a')
        self.cache.set('item4', 'd') # [{4:d}, {3:c}, {2:b}]

        self.assertEqual(self.cache.get('item1'), 'a')  # [{1:a}, {4:d}, {3:c}]
        self.assertEqual(self.cache.get('item3'), 'c')  # [{3:c}, {1:a}, {4:d}]
        self.assertEqual(self.cache.get('item4'), 'd')  # [{4:d}, {1:a}, {3:c}]
        self.assertIsNone(self.cache.get('item2')) 


    def test_cache_nonexistent_retrieval(self):
        self.assertIsNone(self.cache.get('nonexistent'))


if __name__ == '__main__':
    unittest.main()
