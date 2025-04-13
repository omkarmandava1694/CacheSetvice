
import unittest
from cache.entity import Entity
from cache.cache_service import CacheService

class TestCacheService(unittest.TestCase):
    # Setting up a cache service instance with max size = 2.
    def setUp(self):
        self.cache_service = CacheService(3)

    # Test adding an item and retrieving it from cache.
    def test_add_and_get(self):
        e1 = Entity(1, "data1")
        self.cache_service.add(e1)
        self.assertEqual(self.cache_service.get(e1).data, "data1")
        self.assertEqual(self.cache_service.cache_size(), 1)

    # Test for evection when the cache is full
    def test_eviction(self):
        e1 = Entity(1, "data1")
        e2 = Entity(2, "data2")
        e3 = Entity(3, "data3")
        e4 = Entity(4, "data4")
        self.cache_service.add(e1)
        self.cache_service.add(e2)
        self.cache_service.add(e3)
        self.cache_service.add(e4)
        self.assertIsNone(self.cache_service.get(e1))  # e1 should be evicted.
        self.assertEqual(self.cache_service.db_size(), 1)

    # Test for removing single entry from the cache.
    def test_remove(self):
        e1 = Entity(1, "data1")
        self.cache_service.add(e1)
        self.cache_service.remove(e1)
        self.assertIsNone(self.cache_service.get(e1))
        self.assertEqual(self.cache_service.db_size)
    
    # Test case if the entry does not exist
    def test_remove_nonexistent(self):
        e1 = Entity(1, "data1")
        # Try to remove an entity that was never added.
        self.cache_service.remove(e1) # Should not raise exception
        self.assertEqual(len(self.cache_service.cache), 0)
        self.assertEqual(self.cache_service.db_size(), 0)

    # Test cache size after adding elements
    def test_cache_size_after_add(self):
        e1 = Entity(1, "data1")
        e2 = Entity(2, "data2")
        self.cache_service.add(e1)
        self.cache_service.add(e2)
        self.assertEqual(len(self.cache_service.cache), 2)   
    
    # Test case for removing all the entries from cache.
    def test_remove_all_and_clear(self):
        for i in range(3):
            self.cache_service.add(Entity(i, f"Data-{i}"))
        self.cache_service.remove_all()
        self.assertEqual(self.cache_service.cache_size(), 0)
        self.assertEqual(self.cache_service.db_size(), 0)

    # Test case for removing all the 
    def test_clear_only_cache(self):
        e1 = Entity(10, "InDB")
        self.cache_service.database.save(e1)  # Simulate DB save
        self.cache_service.add(e1)
        self.cache_service.clear()
        self.assertEqual(self.cache_service.cache_size(), 0)
        self.assertEqual(self.cache_service.db_size(), 1)

if __name__ == "__main__":
    unittest.main()
