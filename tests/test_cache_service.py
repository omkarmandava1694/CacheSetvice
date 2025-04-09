
import unittest
from cache.entity import Entity
from cache.cache_service import CacheService

class TestCacheService(unittest.TestCase):
    def setUp(self):
        self.cache_service = CacheService(2)

    def test_add_and_get(self):
        e1 = Entity(1, "data1")
        self.cache_service.add(e1)
        self.assertEqual(self.cache_service.get(e1).data, "data1")

    def test_eviction(self):
        e1 = Entity(1, "data1")
        e2 = Entity(2, "data2")
        e3 = Entity(3, "data3")
        self.cache_service.add(e1)
        self.cache_service.add(e2)
        self.cache_service.add(e3)
        self.assertIsNone(self.cache_service.get(e1))  # e1 should be evicted

    def test_remove(self):
        e1 = Entity(1, "data1")
        self.cache_service.add(e1)
        self.cache_service.remove(e1)
        self.assertIsNone(self.cache_service.get(e1))

    def test_remove_all(self):
        e1 = Entity(1, "data1")
        e2 = Entity(2, "data2")
        self.cache_service.add(e1)
        self.cache_service.add(e2)
        self.cache_service.removeAll()
        self.assertIsNone(self.cache_service.get(e1))
        self.assertIsNone(self.cache_service.get(e2))

    def test_clear(self):
        e1 = Entity(1, "data1")
        self.cache_service.add(e1)
        self.cache_service.clear()
        self.assertIsNone(self.cache_service.cache.get(e1.getId()))

if __name__ == "__main__":
    unittest.main()
