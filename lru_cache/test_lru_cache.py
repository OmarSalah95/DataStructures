import unittest
from lru_cache import LRUCache


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(3)

    def test_cache_overwrite_appropriately(self):
        self.cache.set('item1', 'a')
        self.cache.set('item2', 'b')
        self.cache.set('item3', 'c')

        self.cache.set('item2', 'z')

        self.assertEqual(self.cache.get('item1'), 'a')
        self.assertEqual(self.cache.get('item2'), 'z')

    def test_cache_insertion_and_retrieval(self):
        self.cache.set('item1', 'a') # [{1:a}]
        self.cache.set('item2', 'b') # [{2:b}, {1:a}]
        self.cache.set('item3', 'c') # [{3:c}, {2:b}, {1:a}]

        self.assertEqual(self.cache.get('item1'), 'a')
        self.cache.set('item4', 'd') # [{4:d}, {3:c}, {2:b}]

        self.assertEqual(self.cache.get('item1'), 'a') # This should Fail
        self.assertEqual(self.cache.get('item3'), 'c') # This is Golden
        self.assertEqual(self.cache.get('item4'), 'd') # This is golden 
        self.assertIsNone(self.cache.get('item2')) # This and Item 1 are where I am so dang Confused

        """So if I am able to retrieve item 1 which is in my dictionairy and not my cache, yet I am unable to retrieve item 2 which should be in both my dictionary and my cache"""

    def test_cache_nonexistent_retrieval(self):
        self.assertIsNone(self.cache.get('nonexistent'))


if __name__ == '__main__':
    unittest.main()
