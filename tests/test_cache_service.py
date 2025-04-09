
import unittest
from cache.entity import Entity
from cache.cache_service import CacheService

class TestCacheService(unittest.TestCase):
    # Setting up a cache service instance with max size = 2
    def setUp(self):
        self.cache_service = CacheService(2)

    # Test adding an item and retrieving it from cache
    def test_add_and_get(self):
        e1 = Entity(1, "data1")
        self.cache_service.add(e1)
        self.assertEqual(self.cache_service.get(e1).data, "data1")

    # Test for evection when the cache is full
    def test_eviction(self):
        e1 = Entity(1, "data1")
        e2 = Entity(2, "data2")
        e3 = Entity(3, "data3")
        self.cache_service.add(e1)
        self.cache_service.add(e2)
        self.cache_service.add(e3)
        self.assertIsNone(self.cache_service.get(e1))  # e1 should be evicted

    # Test for removing single entry from the cache
    def test_remove(self):
        e1 = Entity(1, "data1")
        self.cache_service.add(e1)
        self.cache_service.remove(e1)
        self.assertIsNone(self.cache_service.get(e1))
    
    # Test case for removing all the entries from cache
    def test_remove_all(self):
        e1 = Entity(1, "data1")
        e2 = Entity(2, "data2")
        self.cache_service.add(e1)
        self.cache_service.add(e2)
        self.cache_service.removeAll()
        self.assertIsNone(self.cache_service.get(e1))
        self.assertIsNone(self.cache_service.get(e2))
    
    # Test case for clearing the cache
    def test_clear(self):
        e1 = Entity(1, "data1")
        self.cache_service.add(e1)
        self.cache_service.clear()
        self.assertIsNone(self.cache_service.cache.get(e1.getId()))

if __name__ == "__main__":
    unittest.main()
